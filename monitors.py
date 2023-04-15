from libqtile.config import Screen
from libqtile import bar, widget
from widgets import widgetlist
from colors import *

import subprocess
import re

widget_defaults = dict(
    font="DejaVu Sans Mono Nerd Font",
    fontsize=13,
    padding=7,
    foreground=col8,
)

screens = []

if int(re.match(
        r"Monitors:\s*(\d+)", 
        subprocess.check_output(["xrandr", "--listmonitors"]).decode()
    )[1]) > 1:
    screens.append(Screen())

screens.append(
    Screen(
        top=bar.Bar(
            widgetlist,
            32,
            background=col1,
        ),
    ),
)
