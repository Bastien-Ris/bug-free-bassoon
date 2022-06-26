# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

################################  Bastien, 20.06.2022
##  ___ _____ ___ _     _____ ##  Separate files: Appearance (bar, colors, theme)
## / _ \_   _|_ _| |   | ____|##  Controls (Apps, Keys, Keychords), Groups
##| | | || |  | || |   |  _|  ##
##| |_| || |  | || |___| |___ ##
## \__\_\|_| |___|_____|_____|##
################################


from typing import List  # noqa: F401

from libqtile import bar, layout, widget, qtile, extension
from libqtile.config import Click, Drag, Group, Match
from libqtile.layout.floating import Floating
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os
import subprocess
from libqtile import hook

from os import path
qtile_path = path.join(path.expanduser("~"), ".config", "qtile")

from controls import *
from appearance import screens, layout_theme, floating_layout_theme, treetab_layout_theme
from mysystem import *
#the following lines define primary settings and hooks
from groups import groups





##----------------------------------------------------
##  LAYOUTS & RULES
##----------------------------------------------------
#
# list deprecated, since layouts are defined on per group
# basis, but useful for the widget and for flexibility,
# as clicking seems to ignore the rules. Or disable click?
#
layouts = [
    layout.Max(**layout_theme),
    layout.MonadTall(**layout_theme),
   	layout.MonadThreeCol(**layout_theme),
    layout.Bsp(**layout_theme, fair=False),
    layout.Floating(**floating_layout_theme),
    layout.TreeTab(**treetab_layout_theme),
    # layout.Columns(**layout_theme),
    # layout.Stack(num_stacks=2, **layout_theme),
    # layout.Spiral(**layout_theme), 
    # layout.Slice(side="bottom", width=400, **layout_theme),
    # layout.MonadWide(**layout_theme),
    # layout.RatioTile(**layout_theme, ratio=1.5),
    # layout.Tile(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Zoomy(**layout_theme),
]

# Drag floating layouts.
mouse = [
	Click([mod], "Button2", lazy.window.toggle_floating()),
	Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
	Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button1", lazy.window.bring_to_front())
]
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = True
cursor_warp = False
floating_layout = layout.Floating(
	**floating_layout_theme,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True


## two hooks stolen from github justinemithies/qtile-x-dotfiles
# When application launched automatically focus it's group
# doesn't wor

@hook.subscribe.client_new
def modify_window(client):
    for group in groups:  # follow on auto-move
        match = next((m for m in group.matches if m.compare(client)), None)
        if match:
            targetgroup = client.qtile.groups_map[group.name]  # there can be multiple instances of a group
            targetgroup.cmd_toscreen(toggle=True)
            break

# Hook to fallback to the first group with windows when last window of group is killed
# Pb: it would fall to Scratchpad in the end, that I want to avoid 
# 


@hook.subscribe.client_killed
def fallback(window):
    if window.group.windows != [window]:
        return
    idx = qtile.groups.index(window.group)
    for group in qtile.groups[idx - 1::-1]:
        if group.windows:
            qtile.current_screen.toggle_group(group)
            return
    qtile.current_screen.toggle_group(qtile.groups[0])


@hook.subscribe.client_new
def set_floating(window):
    if(window.window.get_name() == 'Spotify'):
        window.floating = True
    elif(window.window.get_name() == 'Steam'):
        window.floating = True
    elif(window.window.get_name() == 'galculator'):
        window.floating = True
    elif(window.window.get_name() == 'bastien'):
        window.floating = True


# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None


@hook.subscribe.startup_once
def autostart():
	subprocess.run('/home/bastien/.config/qtile/autostart.sh')


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "Qtile"
