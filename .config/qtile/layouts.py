###########
# Imports #
###########
import re

from libqtile        import layout
from libqtile.config import Match

###########
# Layouts #
###########
layouts = [
    layout.Columns(name="Col", border_focus_stack='#d75f5f', margin=10),
    layout.MonadTall(name="Tall", margin=5),
    layout.MonadWide(name="Wide", margin=5),
    layout.Tile(name="Tile", margin=5),
    layout.TreeTab(name="Tab", margin=5),
]

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(wm_class=re.compile('dialog-.*')), # Custom dialogs
])
