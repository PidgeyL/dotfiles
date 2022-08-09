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


def get_num_monitors():
    num_monitors = 0
    try:
        display = xdisplay.Display()
        screen = display.screen()
        resources = screen.root.xrandr_get_screen_resources()

        for output in resources.outputs:
            monitor = display.xrandr_get_output_info(output, resources.config_timestamp)
            preferred = False
            if hasattr(monitor, "preferred"):
                preferred = monitor.preferred
            elif hasattr(monitor, "num_preferred"):
                preferred = monitor.num_preferred
            if preferred:
                num_monitors += 1
    except Exception as e:
        # always setup at least one monitor
        return 1
    else:
        return num_monitors



screens = [
    Screen(
        wallpaper = WALLPAPER(screen=0),
        wallpaper_mode = "stretch",
        top=bar.Bar(w_main, 24,),
    )]

for i in range(get_num_monitors()-1):
    screens.append(
    Screen(
        wallpaper = WALLPAPER(screen=i+1),
        wallpaper_mode = "stretch"
    ))


widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

