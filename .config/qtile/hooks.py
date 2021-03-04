###########
# Imports #
###########
import os
import subprocess
import sys

from libqtile import hook
sys.path.append(os.path.expanduser('~/.config/qtile/'))

from settings import _AUTORUN_, _check_dependency

################
# Autorun cmds #
################
@hook.subscribe.startup_once
def autostart():
    for prog in _AUTORUN_:
        if _check_dependency(prog):
            subprocess.Popen(prog, shell=True, stdin=None, stdout=None,
                                   stderr=None, close_fds=True)


##########################
# Manipulate new windows #
##########################
@hook.subscribe.client_new
def new_window(window):
    # Resize Kana keyboard
    if window.name == 'KanaKeyboard':
        window.cmd_set_size_floating(600,100)
    if window.name == "DEPENDENCY WARNING":
        window.cmd_set_size_floating(400,50)
