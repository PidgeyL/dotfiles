###########
# Imports #
###########
import os
import sys
from libqtile.config import DropDown, Group, ScratchPad
from libqtile.config import EzKey as Key
from libqtile.lazy   import lazy

sys.path.append(os.path.expanduser('~/.config/qtile/'))

from keys     import keys
from settings import TERMINAL, MUSIC

##################
# Default groups #
##################
groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend([
        Key("A-"+i.name,    lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),
        Key("A-S-"+ i.name, lazy.window.togroup(i.name),   desc="move window to group {}".format(i.name)),
    ])

###############
# Scratchpads #
###############
scratch_settings = {'opacity': 1, 'height': 0.7, 'y': 0.125, 'on_focus_lost_hide': False}
scratchpads = [
    ScratchPad("scratch", [
        DropDown("python", TERMINAL('python3 -q', 'scratch-python'), **scratch_settings),
        DropDown("volume", TERMINAL('pulsemixer', 'scratch-volume'), **scratch_settings),
        DropDown("music",  MUSIC(), **scratch_settings),
    ])
]
groups.extend(scratchpads)
