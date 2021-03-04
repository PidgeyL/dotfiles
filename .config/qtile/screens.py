###########
# Imports #
###########
import os
import sys

from libqtile        import bar, widget
from libqtile.config import Screen

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from settings import WALLPAPER


#######################
# Widgets on main bar #
#######################
w_main = [ widget.CurrentLayout(),
           widget.GroupBox(hide_unused = True),
           widget.Prompt(),
           widget.Spacer(),
           widget.WindowName(max_chars=45),
           widget.Chord(
               chords_colors={
                   'launch': ("#ff0000", "#ffffff"),
               },
               name_transform=lambda name: name.upper(),
           ),
           widget.Sep(),
           widget.Mpd2(status_format="{play_status} {file}"),
           #widget.Volume(emoji=True),
           widget.Sep(),
           widget.Battery(format="🔋 {char} {percent:2.0%}", discharge_char=""),
           widget.Sep(),
           widget.Clock(format='⏲ %H:%M | 📅 %d %h'),
           widget.Sep(),
           widget.Systray(),
]



screens = [
    Screen(
        wallpaper = WALLPAPER(screen=0),
        top=bar.Bar(w_main, 24,),
    ),
]

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

