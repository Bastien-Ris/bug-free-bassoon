

##############################################
##|  _ \_ _/ ___||  _ \| |      / \\ \ / /  ##
##| | | | |\___ \| |_) | |     / _ \\ V /   ##
##| |_| | | ___) |  __/| |___ / ___ \| |    ##
##|____/___|____/|_|   |_____/_/   \_\_|    ##
##############################################

from typing import List  # noqa: F401

from libqtile import bar, layout, widget, qtile, extension
from libqtile.config import Click, Drag, Group, Screen, Match
from libqtile.lazy import lazy
from libqtile.command import lazy
#from libqtile.utils import guess_terminal
import os
import subprocess


# Appearance doesn't not source the variable from controls.py, so update mouse_callbacks
# manually
#The following lines define a color theme depending on Pywal, then general appearances

colors = []
cache='/home/bastien/.cache/wal/colors'
def load_colors(cache):
    with open(cache, 'r') as file:
        for i in range(8):
            colors.append(file.readline().strip())
    colors.append('#ffffff')
    lazy.reload()
load_colors(cache)
   
transparent_color = '#00000000'
background_color = colors[0]
font_color = colors[8]
active_font_color = colors[0]
border_color = colors[3]
focus_color = colors[2]
floating_border_color = colors[7]
floating_focus_color = colors[5]


def init_gradient():    
    return [
        [colors[1], colors[2] ], 
        [colors[2], colors[3] ], 
        [colors[3], colors[4] ], 
        [colors[4], colors[5] ], 
        [colors[5], colors[6] ], 
        [colors[1], colors[3] ], 
        [colors[2], colors[4] ], 
        [colors[1], colors[5] ], 
        ]
gradient = init_gradient()


#### these inits are defined here but used in config.py and screen.py
def init_layout_theme():
	return {"margin":4,
			"border_width":4,
			"border_focus":focus_color,
			"border_normal":border_color,
            }
layout_theme = init_layout_theme()


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

## here start the display

widget_defaults = dict(
    font='Luxi Mono Regular',
    fontsize=12,
    padding=0,
    margin_x=12,
    foreground=font_color
)
extension_defaults = widget_defaults.copy()

panel_height=24



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

   
### defining the unicode separately allows variations, although we also want a general definition
def init_right_arrow():
    return [u"\ue0b4"]
basic_r_arrow = init_right_arrow()

def init_left_arrow():
    return [u"\ue0b6"]
basic_l_arrow = init_left_arrow()

screens = [
    Screen(
        top=bar.Bar(
            [
            *powerline_arrow("l", *basic_l_arrow, transparent_color, colors[1]),
                
            
            widget.Image(filename='~/.config/qtile/icons/python-highcontrast.png',
					mouse_callbacks= {
                    'Button1': lazy.spawn('rofi -show drun'),
                    'Button2': lazy.spawn("kitty"),   
                    'Button3': lazy.run_extension(extension.DmenuRun(**menu_theme))},
					background=colors[1],
					margin_x = 8
                    ),	
             widget.Prompt(prompt="$ => ", background=colors[1], foreground=active_font_color),
            *powerline_arrow("r", *basic_r_arrow, colors[1], background_color),
             
             widget.GroupBox(
					visible_groups=["1","2","3"],
                    hide_unused = False,
                    this_current_screen_border=gradient[0],
                    **groupbox_theme),
            widget.GroupBox(
					visible_groups=["4", "5", "6"],
                    hide_unused = True,
					this_current_screen_border=gradient[3],
                    **groupbox_theme),
            widget.GroupBox(
					visible_groups=["7", "8", "9" ],
                    hide_unused = True,
					this_current_screen_border=gradient[6],
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
                        'Button1':lazy.spawn('kitty -e nvim /home/bastien/.config/qtile/keys.py'),                              
                        'Button3':lazy.spawn('kitty -e nvim /home/bastien/.config/qtile/')}),                               
             widget.Chord(
                        background=background_color,
                        fmt= '{}',
                        fontsize = 18,
                            chords_colors={
                            'layout': (background_color, gradient[0]),
                            'launcher': (background_color, gradient[1]),
                            'silent': (background_color, gradient[2]),
                            'firefox': (background_color, gradient[3]),
                            'web': (background_color, gradient[4]),
                            }
                            ),
             *powerline_arrow("r", *basic_r_arrow, background_color, colors[3]),   

             widget.Image(filename='~/.config/qtile/icons/gtk-select-font.png',
				    mouse_callbacks= { 
					'Button1':lazy.run_extension(extension.DmenuRun(**menu_theme, dmenu_command='clipmenu')),
                    'Button3':lazy.spawn('xclip -selection clipboard blank')},                             
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
                        'Button3':lazy.spawn('xclip -selection clipboard blank')}),                               
       		*powerline_arrow("r", *basic_r_arrow, colors[3], transparent_color),
             
            widget.Spacer(),
            widget.TaskList(
                    background=transparent_color,
                    foreground=font_color,
                    highlight_method='block',
                    unfocused_border=background_color,
					border=gradient[2],
					urgent_border=gradient[7],
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
                        'Button2':lazy.spawn('kitty -e pulsemixer'),
                        'Button3':lazy.spawn('kitty -e alsamixer'),
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
                        'Button3':lazy.spawn('kitty -e alsamixer')}),             
               *powerline_arrow("l", *basic_l_arrow, colors[4], background_color),

                widget.Image(filename='~/.config/qtile/icons/network-transmit-receive.png',
                    background=background_color), 
                widget.Net(background=background_color, format="{up}/{down}"),            
                *powerline_arrow("l", *basic_l_arrow, background_color, colors[5]) ,

                widget.Image(filename='~/.config/qtile/icons/system-run.png',
                    background=colors[5]
                    ),                
                widget.Memory(format='{MemUsed: .0f}{mm}',
					mouse_callbacks= {'Button1': lazy.spawn("kitty -e 'htop'")},
					background=colors[5]
                    ),
                *powerline_arrow("l", *basic_l_arrow, colors[5], background_color),	
                
                widget.Image(filename='~/.config/qtile/icons/cpu.png',
                        background=background_color),
                widget.CPU(format='{load_percent}%  ', 
					mouse_callbacks={'Button1':lazy.spawn('kitty -e bpytop')},
					foreground=font_color,
                    background=background_color,
                    ),
                widget.ThermalSensor(
					tag_sensor='Package id 0',
					mouse_callbacks={'Button1':lazy.spawn('kitty -e bpytop')},
					background=background_color,
                    threshold=60,
                    foreground_alert=colors[5]
                    ),
                *powerline_arrow("l", *basic_l_arrow, background_color, colors[6]),	
               
                widget.Image(filename='~/.config/qtile/icons/hdd.png',
                    background=colors[6]
                    ), 
                widget.DF(partition="/home/", 
					visible_on_warn=False, 
					format='~{uf}{m}', 
					mouse_callbacks={'Button3':lazy.spawn('pcmanfm'), 'Button1':lazy.spawn('kitty -e ranger ~')},
					background=colors[6]
                    ),
                widget.DF(partition="/", 
					visible_on_warn=False, 
					format='/{uf}{m}', 
					mouse_callbacks={'Button3':lazy.spawn('pcmanfm'), 'Button1':lazy.spawn('kitty -e ranger /')},
					background=colors[6]
                    ), 
                widget.DF(partition="/hdd", 
					visible_on_warn=False, 
					format='//{uf}{m}', 
					mouse_callbacks={'Button3':lazy.spawn('pcmanfm'), 'Button1':lazy.spawn('kitty -e ranger /hdd')},
					background=colors[6]
                    ),
                *powerline_arrow("l", *basic_l_arrow, colors[6], background_color),
        
                widget.Clock(format="%a %d %b %H:%M",
                        background=background_color, 
                        padding=3, mouse_callbacks={'Button2':lazy.spawn('thunderbird -calendar')}),
                *powerline_arrow("l", *basic_l_arrow, background_color, colors[7]),
           
              widget.Image(filename='~/.config/qtile/icons/system-shutdown.png',
                    mouse_callbacks= {'Button1': lazy.spawn('rofi -show power-menu -modi "power-menu:rofi-power-menu --choices=shutdown/reboot/logout/lockscreen"')},
                    background=colors[7],
                    margin_x = 8
                    ),
                *powerline_arrow("r", *basic_r_arrow, colors[7], transparent_color),
                
                ],

            panel_height,
            opacity=1,
            border_width=0,
            margin=[4, 4, 2, 4],
            border_color=background_color,
            background=transparent_color,
		),
	),
]