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
azerty = ("<ampersand>", "<eacute>", "<quotedbl>", "<apostrophe>", "<parenleft>", "<section>", "<egrave>", "<exclam>", "<ccedilla>", "<agrave>")
groups = [Group(i) for i in "123456789"]

for i, g in enumerate(groups):
    keys.extend([
        # QWERTY keybinds
        Key("A-"   + g.name, lazy.group[g.name].toscreen(), desc="Switch to group {}".format(g.name)),
        Key("A-S-" + g.name, lazy.window.togroup(g.name),   desc="move window to group {}".format(g.name)),
        # AZERTY keybinds
        Key("A-"   + azerty[i], lazy.group[g.name].toscreen(), desc="Switch to group {}".format(g.name)),
        Key("A-S-" + azerty[i], lazy.window.togroup(g.name),   desc="move window to group {}".format(g.name)),

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
