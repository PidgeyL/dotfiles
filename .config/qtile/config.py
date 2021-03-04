## TODO ##
# * Ability to move windows to the scratchpad
# * Customize layouts a bit
# * Autodetect multiple screens
# * See if using "Max" can be substituted for fullscreen
# * Make selected window stand out more
# * Check config settings for Tile
# * Anki widget
# * Add brightness keys
# * Add media keys for mpd
# * Write missing dependencies to text file

###########
# Imports #
###########
import os
import sys
from typing import List  # noqa: F401

sys.path.append(os.path.expanduser('~/.config/qtile/'))

from keys     import keys                      # type: ignore
from groups   import groups                    # type: ignore
from hooks    import autostart, new_window     # type: ignore
from layouts  import layouts, floating_layout  # type: ignore
from screens  import screens                   # type: ignore
from settings import MUSIC                     # type: ignore


dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "LG3D"

