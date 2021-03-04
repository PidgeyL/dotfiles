###########
# Imports #
###########
import os
import pkgutil
import random
import shutil
import subprocess
import time

from libqtile.lazy   import lazy
from libqtile.utils  import guess_terminal

##############################
# Settings to be set by user #
##############################
_CMD_SPAWN_     = "dmenu_run"
_MUSIC_DEFAULT_ = 'ncmpcpp'
_WALL_SCRIPT_   = "i3wallpaper"
_WALL_LOCATION_ = os.path.expanduser("~/.local/wallpapers")
_AUTORUN_       = ['xcompmgr', 'nm-applet', 'blueman-applet', 'mpd']
_LOCK_SCRIPT_   = "i3lock -e -u -i $(i3wallpaper png lock)"
_REPO_LOCATION_ = os.path.expanduser('~/.local/repos/')
_KANA_LOCATION_ = os.path.join(_REPO_LOCATION_, 'KanaKeyboard/keyboard.py')


################################
# Settings to be used by qtile #
################################
def KANA(qtile):
    if (_check_repo('KanaKeyboard',     critical=True) and
        _check_package('AdvancedInput', critical=True)):
        term = TERMINAL('python3 %s -c'%_KANA_LOCATION_, 'KanaKeyboard', 'dialog-kana')
        qtile.cmd_spawn(term)


def RUNPROMPT(qtile):
    if _check_dependency(_CMD_SPAWN_):
        qtile.cmd_spawn(_CMD_SPAWN_)
    else:
        qtile.cmd_spawncmd("%s Not installed. Spawn"%_CMD_SPAWN_)


def TERMINAL(command=None, name=None, _class=None):
    term = os.getenv("TERMINAL")
    if not term:
        term = guess_terminal()
    if _check_dependency(term):
        if name:    term = term + ' -T %s'%name
        if _class:  term = term + ' -c %s'%_class
        if command: term = term + ' -e %s'%command
        return term


def MUSIC():
    # Check if an env var is set
    music = os.getenv("MUSIC")
    if not music:
        music = _MUSIC_DEFAULT_
    if _check_dependency(music):
        return TERMINAL(music, 'scratch-music')


def WALLPAPER(screen=0):
    # Check if i3 script is present
    if shutil.which(_WALL_SCRIPT_):
        wp = subprocess.getoutput(_WALL_SCRIPT_)
    # Pick random image from wallpaper folder
    else:
        wp = subprocess.getoutput("ls %s/*.*"%_WALL_LOCATION_)
        wp = [i for i in wp if i.lower[-4:] in ('.png', '.jpg', '.gif')]
        if "ls: cannot access" in wp or len(wp) == 0:
            wp = None
        else:
            wp = random.choice(wp.split("\n"))
    return wp


def LOCK(qtile):
    if _check_dependency(_LOCK_SCRIPT_.split()[0], critical=True):
        qtile.cmd_spawn(_LOCK_SCRIPT_)


####################
# Helper Functions #
####################
def _check_dependency(tool, critical=False):
    if shutil.which(tool):
        return True
    else:
        if critical:
            _popup("Dependency not installed: %s"%tool, "DEPENDENCY WARNING", "dependency")
        return False


def _check_repo(repo, critical=False):
    if os.path.isdir(os.path.join(_REPO_LOCATION_, repo)):
        return True
    else:
        if critical:
            _popup("Repo not available: %s"%repo, "DEPENDENCY WARNING", "dependency")
        return False


def _check_package(pkg, critical=True):
    modules = [y.name for y in list(pkgutil.iter_modules())]
    if pkg in modules:
        return True
    else:
        if critical:
            _popup("Python package not installed: %s"%pkg, "DEPENDENCY WARNING", "dependency")
        return False


def _popup(text, name, _class):
    cmd = 'read -n 1 -p "%s"'%text
    prog = TERMINAL(cmd, '"%s"'%name, 'dialog-%s'%_class)
    subprocess.Popen(prog, shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
