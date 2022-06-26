

########################################################################
##    _    ____  ____  _____    _    ____      _    _   _  ____ _____ ##
##   / \  |  _ \|  _ \| ____|  / \  |  _ \    / \  | \ | |/ ___| ____|##
##  / _ \ | |_) | |_) |  _|   / _ \ | |_) |  / _ \ |  \| | |   |  _|  ##
## / ___ \|  __/|  __/| |___ / ___ \|  _ <  / ___ \| |\  | |___| |___ ##
##/_/   \_\_|   |_|   |_____/_/   \_\_| \_\/_/   \_\_| \_|\____|_____|##
########################################################################
from typing import List  # noqa: F401

from libqtile import bar, layout, widget, qtile, extension
from libqtile.config import Click, Drag, Group, Screen, Match
from libqtile.lazy import lazy
from libqtile.command import lazy
from mysystem import *

import os
import subprocess

## !! doesn't source the environment variables set in controls.py, so 
## update mouse_callbacks manually

#The following lines define a color theme depending on Pywal
#    colors 0 to 15, but redundant, here use [
#    0 is white or quasi, 8 is black   
#    with the palet, init gradient generate gradient[0-7]        

colors = []
cache='/home/bastien/.cache/wal/colors'
def load_colors(cache):
    with open(cache, 'r') as file:
        for i in range(8):
            colors.append(file.readline().strip())
    colors.append('#ffffff')
    lazy.reload()
load_colors(cache)


def init_gradient():    
    return [
        [colors[7], colors[1] ],    
        [colors[1], colors[2] ], 
        [colors[2], colors[3] ], 
        [colors[3], colors[4] ], 
        [colors[4], colors[5] ], 
        [colors[5], colors[6] ], 
        [colors[6], colors[7] ], 
        [colors[7], colors[1] ], 
        [colors[1], colors[5] ],      
        ]
gradient = init_gradient()


## some verbal variables, used throughout the config
## for a light theme, set background to 8 and font to 0, and vice-versa
## also a basic canvas for panel and widget, and some settings for the bar

   
transparent_color = '#00000000'
background_color = colors[0]
font_color = colors[8]
active_font_color = colors[0]
border_color = colors[1]
focus_color = colors[4]
floating_border_color = colors[2]
floating_focus_color = colors[5]


widget_defaults = dict(
    font='Luxi Mono Regular',
    fontsize=12,
    padding=0,
    margin_x=12,
    foreground=font_color,
    background=background_color
)
extension_defaults = widget_defaults.copy()

panel_height = 24

def init_bar_theme():
    return{
            "opacity":1,
            "background":transparent_color,
            "margin":[4, 4, 2, 4],
            "border_width":0,
            "border_color":background_color,
            }
bar_theme = init_bar_theme()

### these inits are defined here to use the pywal backend but also used in
### config.py for the layouts and controls.py for the menu
def init_layout_theme():
	return {"margin":4,
			"border_width":4,
			"border_focus":focus_color,
			"border_normal":border_color,
            }
layout_theme = init_layout_theme()

def init_treetab_layout_theme():
    return {
        'font': 'Luxi Mono Regular',
		'fontsize' : 12,
		'sections' : ["", "", ""],
		'section_fontsize' : 12,
		'section_fg': gradient[3],
        'border_width' : 2,
		'bg_color' : background_color,
		'active_bg' : gradient[1],
		'active_fg' : font_color,
		'inactive_bg' : gradient[7],
		'inactive_fg' : font_color,
		'padding_left' : 0,
		'padding_x' : 0,
		'padding_y' : 5,
		'section_top' : 10,
		'section_bottom' : 20,
		'level_shift' : 3,
		'vspace' : 3,
		'panel_width' : 200
            }
treetab_layout_theme = init_treetab_layout_theme()


def init_floating_layout_theme():
	return {"margin":4,
			"border_width":4,
			"border_focus":floating_focus_color,
			"border_normal":floating_border_color,
            }
floating_layout_theme = init_floating_layout_theme()

def init_menu_theme():
	return {"dmenu_lines":12,
			"background":background_color,
		    "foreground":font_color,
			"selected_background":focus_color,
			"font":'Luxi Mono Regular',
			"fontsize":12,
			"dmenu_prompt":'>>',
			"dmenu_ignorecase":True				
			}			
menu_theme = init_menu_theme()

def init_groupbox_theme():
    return {
           "active" : gradient[0],
			"inactive": font_color,
            "rounded" :True,
            "highlight_method" : 'border',
            "fontsize" : 14,
			"urgent_border" : floating_border_color,
			"urgent_text" : floating_focus_color,
			"background" : background_color,
            }
groupbox_theme = init_groupbox_theme()

## 
## place for some deco !
## textxy stands unicode char and can be defined in init_right/left_arrow
## separately or for each arrow. see Nerd Fonts


def powerline_arrow(direction, textxy, color1, color2):
    if direction == "r":
        return [
            widget.Sep(padding=0, linewidth=0, background=color2),
            widget.TextBox(
				font='FantasqueSansMono Nerd Font',
                text=textxy,
                padding=0,
                foreground=color1,
                background=color2,
                fontsize=panel_height,
            ),
        ]
    else:
        return [
            widget.TextBox(
				font='FantasqueSansMono  Nerd Font',
                text=textxy,
                foreground=color2,
                padding=0,
                background=color1,
                fontsize=panel_height,),
            widget.Sep(padding=0, linewidth=0, background=color1),
        ]

def double_powerline_arrow(direction, textxy, color1, color2, color3):
     if direction == "r":
        return [
            *powerline_arrow(direction, textxy, color1, color2),
            widget.Sep(padding=0, linewidth=0, background=color2),
            *powerline_arrow(direction, textxy, color2, color3),
         ]
     else:
        return [
            *powerline_arrow(direction, textxy, color3, color2),
            widget.Sep(padding=0, linewidth=0, background=color2),
            *powerline_arrow(direction, textxy, color2, color1),
         ]

   
def init_right_arrow():
    return [u"\ue0c6"]
basic_r_arrow = init_right_arrow()

def init_left_arrow():
    return [u"\ue0c7"]
basic_l_arrow = init_left_arrow()



##############################################################################
##############################################################################
###  here we really create the bar with the widgets 

screens = [
    Screen(
        top=bar.Bar(
            [
            *powerline_arrow("l", *basic_l_arrow, transparent_color, colors[1]),
                
            
            widget.Image(filename='~/.config/qtile/icons/python-highcontrast.png',
					mouse_callbacks= {
                    'Button1': lazy.spawn('rofi -show drun'),
                    'Button2': lazy.spawn(terminal),   
                    'Button3': lazy.run_extension(extension.DmenuRun(**menu_theme))},
					background=colors[1],
					margin_x = 8
                    ),	
             widget.Prompt(prompt="$ => ", background=colors[1], foreground=active_font_color),
            *powerline_arrow("r", *basic_r_arrow, colors[1], background_color),
             
             widget.GroupBox(
					visible_groups=["1","2","3","4","5"],
                    hide_unused = False,
                    this_current_screen_border=gradient[1],
                    **groupbox_theme),
            widget.GroupBox(
					visible_groups=[ "6", "7", "8", "9" ],
                    hide_unused = True,
					this_current_screen_border=gradient[5],
                    **groupbox_theme),
            *powerline_arrow("r", *basic_r_arrow, background_color, colors[2]),
            	
                         
             widget.CurrentLayoutIcon(
                    custom_icon_paths= ['/home/bastien/.config/qtile/icons/'],
                    background=colors[2],
                    padding = 8,
                    scale=0.8,
				    ),
             *powerline_arrow("r", *basic_r_arrow, colors[2], background_color),
                
             widget.Image(filename='~/.config/qtile/icons/vim.png',
                      background=background_color,
                      margin_x = 15,
				  mouse_callbacks={
                        'Button1':lazy.spawn( myapplications["v"]), 
                        'Button3':lazy.spawn(myapplications["v"] + "  ~/.config/qtile/")}),                               
             widget.Chord(
                        background=background_color,
                        fmt= '{}',
                        fontsize = 18,
                            chords_colors={
                            mymodes[0] : (background_color, gradient[0]),
                            mymodes[1] : (background_color, gradient[2]),
                            mymodes[2] : (background_color, gradient[4]),
                            mymodes[3] : (background_color, gradient[6]),
                            mymodes[4] : (background_color, gradient[3]),
                            }
                            ),
             *powerline_arrow("r", *basic_r_arrow, background_color, colors[3]),   

             widget.Image(filename='~/.config/qtile/icons/gtk-select-font.png',
				    mouse_callbacks= { 
					'Button1':lazy.run_extension(extension.DmenuRun(**menu_theme, dmenu_command='clipmenu')),
                        },                             
                    background=colors[3],
                    margin_x = 8 
                    ), 
              widget.Clipboard(
					fmt='{}',
					fontsize=12,
					foreground=font_color,
					background=colors[3],
					max_width=96,
					timeout=4, 
					mouse_callbacks={
                        'Button1':lazy.run_extension(extension.DmenuRun(**menu_theme, dmenu_command='clipmenu')),
                        'Button1':lazy.run_extension(extension.DmenuRun(**menu_theme, dmenu_command='clipmenu'))}),                               
       		*powerline_arrow("r", *basic_r_arrow, colors[3], transparent_color),
             
            widget.Spacer(),
            widget.TaskList(
                    background=transparent_color,
                    foreground=font_color,
                    highlight_method='block',
                    unfocused_border=background_color,
					border=colors[2],
					urgent_border=colors[7],
					max_title_width=75,
                    padding=4,
					rounded=True,
					markup=True,
					markup_minimized="<b>{}</b>"),
            widget.Spacer(),

    
             *powerline_arrow("l", *basic_l_arrow, transparent_color, colors[4]),
             widget.Image(filename='~/.config/qtile/icons/emblem-music.png',
				    background=colors[4],
                    margin_x=8,
                       mouse_callbacks={
                        'Button1':lazy.spawn('bash /home/bastien/.config/qtile/pulse-audio-notify.sh mute'), 
                        'Button2':lazy.spawn(myapplications['XF86AudioRaiseVolume']),
                        'Button3':lazy.spawn(myapplications['XF86AudioLowerVolume']),
                        'Button4':lazy.spawn('bash /home/bastien/.config/qtile/pulse-audio-notify.sh up'), 
                        'Button5':lazy.spawn('bash /home/bastien/.config/qtile/pulse-audio-notify.sh down')
                    }),
               widget.Volume(
				    #theme_path = ['home/bastien/.config/qtile/icons/'],
                    fmt = '{} ',    
                    emoji = False,
                    foreground=font_color,
                    background=colors[4],
                    volume_app='pulsemixer',
                    volume_down_command = 'bash /home/bastien/.config/qtile/pulse-audio-notify.sh down',
                    volume_up_command = 'bash /home/bastien/.config/qtile/pulse-audio-notify.sh up',
                    mute_command = 'bash /home/bastien/.config/qtile/pulse-audio-notify.sh mute',
					mouse_callbacks={
                        'Button1':lazy.spawn(myapplications["XF86AudioRaiseVolume"]),
                        'Button3':lazy.spawn(myapplications["XF86AudioLowerVolume"])}),             
               *powerline_arrow("l", *basic_l_arrow, colors[4], background_color),

                widget.Image(filename='~/.config/qtile/icons/network-transmit-receive.png',
                    background=background_color), 
               widget.Net(foreground=font_color,
                        background=background_color, 
                        format="{up}/{down}"),            
                *powerline_arrow("l", *basic_l_arrow, background_color, colors[5]) ,

                widget.Image(filename='~/.config/qtile/icons/system-run.png',
                    background=colors[5]
                    ),                
                widget.Memory(format='{MemUsed: .0f}{mm}',
					mouse_callbacks= {'Button1': lazy.spawn(myapplications['h'])},
					background=colors[5],
                    foreground=font_color),
                *powerline_arrow("l", *basic_l_arrow, colors[5], background_color),	
                
                widget.Image(filename='~/.config/qtile/icons/cpu.png',
                        background=background_color),
                widget.CPU(format='{load_percent}%  ', 
					mouse_callbacks={'Button1':lazy.spawn(myapplications['t'])},
					foreground=font_color,
                    background=background_color,
                    ),
                widget.ThermalSensor(
					tag_sensor='Package id 0',
					mouse_callbacks={'Button1':lazy.spawn(myapplications['t'])},
					background=background_color,
                    threshold=60,
                    foreground=font_color,
                    foreground_alert=colors[5]
                    ),
                *powerline_arrow("l", *basic_l_arrow, background_color, colors[6]),	
               
                widget.Image(filename='~/.config/qtile/icons/hdd.png',
                    background=colors[6]
                    ), 
                widget.DF(partition="/home/", 
					visible_on_warn=False, 
					format='~{uf}{m}', 
					foreground=font_color,
                    mouse_callbacks={'Button1':lazy.spawn(myapplications['r'])},
					background=colors[6]
                    ),
                widget.DF(partition="/", 
					visible_on_warn=False, 
					format='/{uf}{m}', 
					mouse_callbacks={'Button1':lazy.spawn(myapplications['r'] + " /")},
					background=colors[6],
                    foreground=font_color,
                    ), 
                widget.DF(partition="/hdd", 
					visible_on_warn=False, 
					format='//{uf}{m}', 
					mouse_callbacks={'Button1':lazy.spawn(myapplications['r'] + " /hdd")},
					background=colors[6],
                    foreground=font_color,
                    ),
                *powerline_arrow("l", *basic_l_arrow, colors[6], background_color),
        
                widget.Clock(format="%a %d %b %H:%M",
                        background=background_color, 
                        foreground=font_color,
                        padding=3, 
                        mouse_callbacks={'Button2':lazy.spawn('thunderbird -calendar')}),
                *powerline_arrow("l", *basic_l_arrow, background_color, gradient[7]),
           
              widget.Image(filename='~/.config/qtile/icons/system-shutdown.png',
                    mouse_callbacks= {'Button1': lazy.spawn('rofi -show power-menu -modi "power-menu:rofi-power-menu --choices=shutdown/reboot/logout/lockscreen"')},
                    background=gradient[7],
                    margin_x = 8
                    ),
                *powerline_arrow("r", *basic_r_arrow, gradient[7], transparent_color),
                ],
           panel_height,
           **bar_theme,
         ),
	),
]
