from libqtile import widget
from libqtile.lazy import lazy
from colors import *

widgetlist=[
    widget.GroupBox(
        font="DejaVu Bold",
        highlight_method="block",
        this_current_screen_border=col_mid,
        this_screen_border=col_bg,
        other_current_screen_border=col_mid,
        other_screen_border=col_bg,
        active=col6,
        inactive=col8,
    ),
    # widget.Spacer(),
    widget.WindowName(
    ),
    widget.Spacer(),
    widget.Systray(),
    widget.Spacer(length=5),
    #widget.Wlan(
    #    fmt="  {} ",
    #),
    widget.Backlight(
       backlight_name="intel_backlight", 
       fmt=" {} ",
    ),
    #widget.Bluetooth(
    #    fmt=" {} ",
    #    mouse_callbacks={"Button1" : lazy.spawn("blueman-manager")},
    #    hci="/dev_4C_36_4E_9F_A3_2A",
    #),
     widget.Battery(
        format=" {percent:2.0%}"
    ),
    widget.CPU(
        fmt=" {}",
        format="{freq_current}GHz {load_percent}%",
    ),
    widget.Memory(
        fmt=" {}",
        format="{MemUsed:.2f}{mm} {MemPercent}%",
        measure_mem="G",
    ),
    widget.DF(
        fmt=" {}",
        format="{f}{m} {r:.0f}%",
        visible_on_warn=False,
    ),
    widget.PulseVolume(
        fmt = "蓼 {}",
        mouse_callbacks={"Button1" : lazy.spawn("pavucontrol")}, 
    ),
    widget.Clock(
        format="  %a, %d.%m.%Y %H:%M",
    ),
    widget.QuickExit(
        default_text=" ",
    ),
]

#for i, e in enumerate(widgetlist[-5:]):
#    e.foreground = col1
#    e.background = collist[1:][i % (len(collist)-1)]
