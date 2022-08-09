###########
# Imports #
###########
import os
import sys

from libqtile.config import EzKey as Key
from libqtile.lazy   import lazy

sys.path.append(os.path.expanduser('~/.config/qtile/'))

from settings import RUNPROMPT, KANA, TERMINAL, LOCK

###############
# Keybindings #
###############
keys = [
    # Switch between windows
    Key("A-h",         lazy.layout.left(),              desc="Move focus left"),
    Key("A-<Left>",    lazy.layout.left(),              desc="Move focus left"),
    Key("A-l",         lazy.layout.right(),             desc="Move focus right"),
    Key("A-<Right>",   lazy.layout.right(),             desc="Move focus right"),
    Key("A-j",         lazy.layout.down(),              desc="Move focus down"),
    Key("A-<Down>",    lazy.layout.down(),              desc="Move focus down"),
    Key("A-k",         lazy.layout.up(),                desc="Move focus up"),
    Key("A-<Up>",      lazy.layout.up(),                desc="Move focus up"),

    # Move windows
    Key("A-S-h",       lazy.layout.shuffle_left(),      desc="Move window left"),
    Key("A-S-<Left>",  lazy.layout.shuffle_left(),      desc="Move window left"),
    Key("A-S-l",       lazy.layout.shuffle_right(),     desc="Move window right"),
    Key("A-S-<Right>", lazy.layout.shuffle_right(),     desc="Move window right"),
    Key("A-S-j",       lazy.layout.shuffle_down(),      desc="Move window down"),
    Key("A-S-<Down>",  lazy.layout.shuffle_down(),      desc="Move window down"),
    Key("A-S-k",       lazy.layout.shuffle_up(),        desc="Move window up"),
    Key("A-S-<Up>",    lazy.layout.shuffle_up(),        desc="Move window up"),

    # Grow windows.
    Key("A-C-h",       lazy.layout.grow_left(),         desc="Grow window left"),
    Key("A-C-<Left>",  lazy.layout.grow_left(),         desc="Grow window left"),
    Key("A-C-l",       lazy.layout.grow_right(),        desc="Grow window right"),
    Key("A-C-<Right>", lazy.layout.grow_right(),        desc="Grow window right"),
    Key("A-C-j",       lazy.layout.grow_down(),         desc="Grow window down"),
    Key("A-C-<Down>",  lazy.layout.grow_down(),         desc="Grow window down"),
    Key("A-C-k",       lazy.layout.grow_up(),           desc="Grow window up"),
    Key("A-C-<Up>",    lazy.layout.grow_up(),           desc="Grow window up"),
    Key("A-C-n",       lazy.layout.normalize(),         desc="Reset window sizes"),
    Key("A-C-<space>", lazy.window.toggle_fullscreen(), desc="Toggle Fullscreen"),
    Key("A-C-o", lazy.layout.maximize(), desc="Toggle Fullscreen"),

    # Other system keys
    Key("A-<Tab>",     lazy.next_layout(),              desc="Toggle layouts"),
    Key("A-S-q",       lazy.window.kill(),              desc="Kill window"),
    Key("A-S-r",       lazy.restart(),                  desc="Restart Qtile"),
    Key("A-S-e",       lazy.shutdown(),                 desc="Shutdown Qtile"),
    Key("A-d",         lazy.function(RUNPROMPT),        desc="Run command"),
    Key("A-<Return>",  lazy.spawn(TERMINAL()),          desc="Launch terminal"),
    Key("M-l",         lazy.function(LOCK),             desc="Launch terminal"),

    # Multimedia keys
    Key('<XF86AudioRaiseVolume>', lazy.spawn('pmctl volume raise 10')),
    Key('<XF86AudioLowerVolume>', lazy.spawn('pmctl volume lower 10')),
    Key('<XF86AudioMute>',        lazy.spawn('pmctl mute toggle')),

    # Scratchpads & Custom programs
    Key('A-S-p',       lazy.group['scratch'].dropdown_toggle('python')),
    Key('A-S-m',       lazy.group['scratch'].dropdown_toggle('music')),
    Key('A-S-a',       lazy.group['scratch'].dropdown_toggle('volume')),
    Key('M-k',         lazy.function(KANA) ),

    Key('A-s', lazy.next_screen()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key("A-S-<Return>", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

]

