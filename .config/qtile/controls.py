####################################################
##____ ___  _   _ _____ ____   ___  _     ____    ##
## / ___/ _ \| \ | |_   _|  _ \ / _ \| |   / ___| ##
##| |  | | | |  \| | | | | |_) | | | | |   \___ \ ##
##| |__| |_| | |\  | | | |  _ <| |_| | |___ ___) |##
## \____\___/|_| \_| |_| |_| \_\\___/|_____|____/ ##
####################################################

from libqtile.config import Key, KeyChord, Screen, Group, ScratchPad, DropDown
from libqtile.command import lazy 
from libqtile import extension
from groups import groups
from appearance import menu_theme
from libqtile import hook 
from mysystem import * 

###############################################################################
#### define some keys
###############################################################################

### 
### in this config, alt and ctrl are not used 
### "asdw" are already used. 
### "Up", "Down", "Left", "Right" 
###  are an option. For Gnu/emacs kind of stuff, must remap everything

mod = "mod4"
up = "k"
down = "j"
left = "h"
right = "l"


##############################################################################
##    Functions that generate embedded key tables in the keychords
#################################################################################
def launch_apps(applications):
    custom_keys = []
    for shortcuts in applications:
        custom_keys.append(Key([], shortcuts, lazy.spawn(applications[shortcuts])),)  
    return custom_keys              


def browse_the_web(browser, websites):
    custom_keys = []
    for entries in websites:
        custom_keys.append(Key([], entries, lazy.spawn(browser + " " + websites[entries])),)  
    return custom_keys              

def move_between_groups(groups):
    groups = [Group(i) for i in "123456789eogfvi"]
    custom_keys = []
    for i in groups:                                                                
        custom_keys.append(Key([], i.name, lazy.window.togroup(i.name, switch_group=False),
                desc="move focused window to group {}".format(i.name)),)
        custom_keys.append(Key([mod], i.name, lazy.window.togroup(i.name, switch_group=True),
                 desc="move focused window to group {} & switch".format(i.name)),)
    return custom_keys


############################################################################### 
##     basic_stuff and media keys are available in all modes except "silent", list 
## here to avoid repetitions
###############################################################################

def init_media_keys():
    return{
          
        Key([], "XF86AudioMute", lazy.spawn('bash /home/bastien/.config/qtile/pulse-audio-notify.sh mute')),
        Key([], "XF86AudioLowerVolume", lazy.spawn('bash /home/bastien/.config/qtile/pulse-audio-notify.sh down')),
        Key([], "XF86AudioRaiseVolume", lazy.spawn('bash /home/bastien/.config/qtile/pulse-audio-notify.sh up')),
        Key([mod], "XF86AudioLowerVolume", lazy.spawn('bash /home/bastien/.config/qtile/pulse-audio-notify.sh down+')),
        Key([mod], "XF86AudioRaiseVolume", lazy.spawn('bash /home/bastien/.config/qtile/pulse-audio-notify.sh up+')),
    
        #Key([], "XF86AudioMute", lazy.spawn('amixer -q set Master toggle')),
        #Key([], "XF86AudioLowerVolume", lazy.spawn('amixer -c 0 sset Master 5- unmute')),
        #Key([], "XF86AudioRaiseVolume", lazy.spawn('amixer -c 0 sset Master 5+ unmute')),
        #Key([mod], "XF86AudioLowerVolume", lazy.spawn('amixer -q set %s 20%%')),
        #Key([mod], "XF86AudioRaiseVolume", lazy.spawn('amixer -q set %s 80%%')),
    
        Key([], "XF86AudioNext", lazy.spawn('dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Next')),
        Key([], "XF86AudioPrev", lazy.spawn('dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.Previous')),
        Key([], "XF86AudioPlay", lazy.spawn('dbus-send --print-reply --dest=org.mpris.MediaPlayer2.spotify /org/mpris/MediaPlayer2 org.mpris.MediaPlayer2.Player.PlayPause')),
        Key([], "XF86HomePage", lazy.spawn("rofi -modi drun,window -show drun"), desc="launch gnome-like app-launcher"),
    
        Key([], "XF86Calculator", lazy.group['scratch'].dropdown_toggle('math')),

          
        Key([], "XF86Mail", lazy.group['scratch'].dropdown_toggle('mails')), 
        Key([], "XF86Explorer", lazy.group['scratch'].dropdown_toggle('files')),
        }
media_keys = init_media_keys()



def init_basic_stuff():
    return{
        
        Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
        Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
        Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"), 
        Key([mod], "p", lazy.run_extension(extension.DmenuRun(**menu_theme, dmenu_command='clipmenu'))),
        Key([], "Print", lazy.spawn('/home/bastien/.config/qtile/screenshot.sh')),
        Key([mod], "Print", lazy.spawn('/home/bastien/.config/qtile/screenshot_select.sh')),
        

        Key([], 'F10', lazy.group['scratch'].dropdown_toggle('music')), 
        Key([], 'F12', lazy.group['scratch'].dropdown_toggle('term')),
        Key([], 'F11', lazy.group['scratch'].dropdown_toggle('web')), 
        }
basic_stuff = init_basic_stuff()

def init_layout_mode():
    return{
            Key([], "space", lazy.hide_show_bar(), desc="Toggle visibility of Bar"),
            Key([], "Left", lazy.screen.prev_group(skip_empty=True)), # cycle left   
            Key([], "Right", lazy.screen.next_group(skip_empty=True)), #cycle right
            Key([], 'Up', lazy.window.toggle_minimize()),
            Key([], 'Down', lazy.window.toggle_fullscreen()), 
            
            
            Key([], left, lazy.layout.left(), desc="Move focus to left"),
            Key([], right, lazy.layout.right(), desc="Move focus to right"),
            Key([], down, lazy.layout.down(), desc="Move focus down"),
            Key([], up, lazy.layout.up(), desc="Move focus up"),
                   
            Key([], "a", lazy.layout.grow_left(), desc="Grow window to the left"),
            Key([], "d", lazy.layout.grow_right(), desc="Grow window to the right"),
            Key([], "s", lazy.layout.grow_down(), desc="Grow window down"),
            Key([], "w", lazy.layout.grow_up(), desc="Grow window up"),
            

            Key([], "x", lazy.layout.grow_main(), desc="increase ratio master/slave"),
            Key([], "y", lazy.layout.shrink_main(), desc="decrease ratio master/slave"), 
            Key([], "m", lazy.layout.maximize()),
            Key([], "n", lazy.layout.normalize()),
            Key([], "c", lazy.window.kill(), desc="kill focus window"), 
            
            Key([mod], left, lazy.layout.shuffle_left(), desc="Move window to the left"),
            Key([mod], right, lazy.layout.shuffle_right(), desc="Move window to the right"),
            Key([mod], left, lazy.layout.swap_left()),  ##Monadtall specific
	        Key([mod], right, lazy.layout.swap_right()), ## monadtall specific
            Key([mod], down, lazy.layout.shuffle_down(), desc="Move window down"),
            Key([mod], up, lazy.layout.shuffle_up(), desc="Move window up"),
	      

            ## floating windows rules
            Key([], "KP_Insert", lazy.window.toggle_floating()),

            Key([mod], "KP_Down", lazy.window.resize_floating(0, 25), desc="resize floating window to the right"),
            Key([mod], "KP_Up", lazy.window.resize_floating(0, -25), desc="resize fl. window to the right"),
	        Key([mod], "KP_Left", lazy.window.resize_floating(-25, 0), desc="resize floating window to the left"),
            Key([mod], "KP_Right", lazy.window.resize_floating(25, 0), desc="resize floating window to the right"),
            
            Key([], "KP_Right", lazy.window.move_floating(25,0), desc="Move floating window to the right"),
            Key([], "KP_Left", lazy.window.move_floating(-25,0), desc="Move floating window to the right"),
	        Key([], "KP_Up", lazy.window.move_floating(0,-25), desc="Move floating window upwards"),
            Key([], "KP_Down", lazy.window.move_floating(0,25), desc="Move floating window downwards"),
            

            
            ### Treetab controls
            Key([mod], "a", lazy.layout.section_up(),
             desc='Move up a section in treetab'),
            Key([mod], "d", lazy.layout.section_down(),
             desc='Move up a section in treetab'),
            Key([mod], "w", lazy.layout.move_up(), 
                desc='Move down a section in treetab'),
            Key([mod], "s", lazy.layout.move_down(), 
                desc='Move down a section in treetab'),

            #those are for BSP
	        Key([mod], "a", lazy.layout.flip_left()),
	        Key([mod], "d", lazy.layout.flip_right()),
            Key([mod], "s", lazy.layout.flip_down()),
	        Key([mod], "w", lazy.layout.flip_up()),
	        Key([mod], "space", lazy.layout.flip()),
            
 
            Key([], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
            Key([mod], "Tab", lazy.prev_layout(), desc="Toggle between layouts"),
            *move_between_groups(groups)
            }
layout_mode= init_layout_mode()

##############################################################################
######                          here start the keys
##############################################################################

keys = [
   
    *media_keys,
    *basic_stuff,   

    
    Key([mod], "Left", lazy.screen.prev_group(skip_empty=True)), # cycle left   
    Key([mod], "Right", lazy.screen.next_group(skip_empty=True)), #cycle right
    Key([mod], 'Up', lazy.window.toggle_minimize()),
    Key([mod], 'Down', lazy.window.toggle_fullscreen()), 
    Key([mod], "KP_Insert", lazy.window.toggle_floating()), 
    
    # add some window navigation and simple things for the normal mode
    Key([mod], left, lazy.layout.left(), desc="Move focus to left"),
    Key([mod], right, lazy.layout.right(), desc="Move focus to right"),
    Key([mod], down, lazy.layout.down(), desc="Move focus down"),
    Key([mod], up, lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move focus to next window"),

     
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "w", lazy.spawn('/home/bastien/.config/qtile/change_theme.sh')),
    Key([mod, "shift"], "Delete", lazy.spawn('rofi -show power-menu -modi "power-menu:rofi-power-menu --choices=shutdown/reboot/logout/lockscreen"')),

  
        ##window mode - now I try to implement a single keychord and a full mode
    KeyChord([mod], "w", [
            

        *layout_mode,
        *media_keys,
        *basic_stuff,

        
        KeyChord([mod], "w", [
                
            *layout_mode,
            *media_keys,
            *basic_stuff,
           #Key([mod], "w", lazy.ungrab_chord()),
       ], mode=mymodes[0]),

    ]),

    #applications
    KeyChord([mod], "a", [
            
        *launch_apps(myapplications),
        *media_keys,
        *basic_stuff,

        KeyChord([mod], "a", [

            *launch_apps(myapplications),
            *media_keys,
            *basic_stuff,
           #Key([mod], "a", lazy.ungrab_chord()),   
        ], mode=mymodes[1]),
    ]),

    KeyChord([mod], "d", [

       *browse_the_web(mybrowser, mywebsites),
       *media_keys,
       *basic_stuff,

       KeyChord([mod], "d", [

           *browse_the_web(mybrowser, mywebsites),
           *media_keys,
           *basic_stuff,
          #Key([mod], "d", lazy.ungrab_chord()),
       ], mode=mymodes[2]),
    ]),    

    KeyChord([mod], "f", [

        KeyChord([mod], "f", [ 
   
            *browse_the_web(mysecondbrowser, mywebsites),
            *media_keys,
            *basic_stuff,
            #Key([mod], "f", lazy.ungrab_chord()),      
        ], mode=mymodes[3]),
    ]),    

    KeyChord([mod], "s", [
            
            Key([mod], "s", lazy.ungrab_chord()),
           
            ], mode= mymodes[4],
    ),    
]

groups = [Group(i) for i in "123456789eogfvi"] 
for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),
    ])

