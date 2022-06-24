####################################################
##____ ___  _   _ _____ ____   ___  _     ____    ##
## / ___/ _ \| \ | |_   _|  _ \ / _ \| |   / ___| ##
##| |  | | | |  \| | | | | |_) | | | | |   \___ \ ##
##| |__| |_| | |\  | | | |  _ <| |_| | |___ ___) |##
## \____\___/|_| \_| |_| |_| \_\\___/|_____|____/ ##
####################################################

from libqtile.config import Key, KeyChord, Screen
from libqtile.command import lazy 
from libqtile import extension
from groups import groups
from appearance import menu_theme
from libqtile import hook 

###############################################################################
#### define some variables
###############################################################################

### in this config, asdw are already used. "Up", "Down", "Left", "Right" 
###  are an option. For Gnu/emacs kind of stuff, that woudn't work
###  alt and ctrl are not used in this config 

mod = "mod4"
up = "k"
down = "j"
left = "h"
right = "l"

## write apps-name as a launch command (for example "spotify --minimized")
## the dictionary keys are used to generate the keybindings
## through use of modes and keychords, keybinds for applications, websites or 
## groups don't overlap, so you can map "1", "a", or  to a group, a website and 
## an app 
##

terminal = "kitty"

mybrowser = "luakit"
mysecondbrowser = "firefox"

myapplications = {

   "p" : "pcmanfm",                                
   "e" : "emacs",                                  
   "v" : "kitty -e nvim",                          
   "l" : "libreoffice",                            
   "z" : "zathura",                                
   "g" : "gimp",                                   
   "i" : "inkscape",                               
   "w" : "vmware-view",                            
   "f" : mysecondbrowser,                                       ##                                  
   "b" : mybrowser,                                
   "h" : "kitty -e 'htop'",                        
   "t" : "kitty -e 'bpytop'", 
   "g" : "gimp",
        }

mywebsites = {
    "y" : "www.youtube.com",
    "w" : "www.wikipedia.com",
    "g" : "www.gentoo.org",
    "a" : "www.wiki.archlinux.org",
    "l" : "www.gitlab.com",
    "h" : "www.github.com"
}

## mode_names
def init_modes():
    return [
            "layout",    ##first mode : window and group controls, mod + w
            "launch",    ##second mode : run applications based on dictionary "myapplications", mod + a   
            "browser",    ##third mod    
            "firefox",   ##fourth mode, the same as third but with a second browser   
            "silent"
            ]
mymodes = init_modes()

###############################################################################
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
    
        Key([], "XF86Calculator", lazy.spawn('galculator')),

          
        Key([], "XF86Mail", lazy.group['0'].dropdown_toggle('mails')), 
        Key([], "XF86Explorer", lazy.group['0'].dropdown_toggle('files')),
        }
media_keys = init_media_keys()



def init_basic_stuff():
    return{
        
        Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
        Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
        Key([mod], 'q', lazy.window.toggle_minimize()),
        Key([mod], 'e', lazy.window.toggle_fullscreen()), 
        Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"), 
        Key([mod], "p", lazy.run_extension(extension.DmenuRun(**menu_theme, dmenu_command='clipmenu'))),
        Key([], "Print", lazy.spawn('/home/bastien/.config/qtile/screenshot.sh')),
        Key([mod], "Print", lazy.spawn('/home/bastien/.config/qtile/screenshot_select.sh')),
        

        Key([], 'F10', lazy.group['0'].dropdown_toggle('music')), 
        Key([], 'F12', lazy.group['0'].dropdown_toggle('term')),
        Key([], 'F11', lazy.group['0'].dropdown_toggle('web')), 
        }
basic_stuff = init_basic_stuff()

##############################################################################
######                          here start the keys
##############################################################################

keys = [
    # Reorganise pro mode? the keychords aim to avoid conflicts with other things, although emacs is easily messing aroung   
   
    *media_keys,
    *basic_stuff,   


        # window navigation
    Key([mod], left, lazy.layout.left(), desc="Move focus to left"),
    Key([mod], right, lazy.layout.right(), desc="Move focus to right"),
    Key([mod], down, lazy.layout.down(), desc="Move focus down"),
    Key([mod], up, lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move focus to next window"),
     
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "w", lazy.spawn('/home/bastien/.config/qtile/change_theme.sh')),
    Key([mod, "shift"], "Delete", lazy.spawn('rofi -show power-menu -modi "power-menu:rofi-power-menu --choices=shutdown/reboot/logout/lockscreen"')),

    #Key([mod], "d", lazy.run_extension(extension.DmenuRun(**menu_theme))),
   
    # KeyChord([mod], "d", [
   #         ], mode= "dmenu"
   # ),      
        ##window mode
    KeyChord([mod], "w", [
            
            Key([mod], "w", lazy.ungrab_chord()), 
            
            *media_keys,
            *basic_stuff,

            Key([], left, lazy.layout.left(), desc="Move focus to left"),
            Key([], right, lazy.layout.right(), desc="Move focus to right"),
            Key([], down, lazy.layout.down(), desc="Move focus down"),
            Key([], up, lazy.layout.up(), desc="Move focus up"),
            Key([], "space", lazy.layout.next()),
        
            Key([], "a", lazy.layout.grow_left(), desc="Grow window to the left"),
            Key([], "d", lazy.layout.grow_right(), desc="Grow window to the right"),
            Key([], "w", lazy.layout.grow_down(), desc="Grow window down"),
            Key([], "s", lazy.layout.grow_up(), desc="Grow window up"),
            
            Key([], "x", lazy.layout.grow_main(), desc="increase ratio master/slave"),
            Key([], "y", lazy.layout.shrink_main(), desc="decrease ratio master/slave"), 

            Key([mod], left, lazy.layout.shuffle_left(), desc="Move window to the left"),
            Key([mod], right, lazy.layout.shuffle_right(), desc="Move window to the right"),
            Key([mod], left, lazy.layout.swap_left()),  ##Monadtall specific
	        Key([mod], right, lazy.layout.swap_right()), ## monadtall specific
            Key([mod], down, lazy.layout.shuffle_down(), desc="Move window down"),
            Key([mod], up, lazy.layout.shuffle_up(), desc="Move window up"),
	       

            #those are for BSP
	        Key([mod], "z", lazy.layout.flip_left()),
	        Key([mod], "o", lazy.layout.flip_right()),
            Key([mod], "u", lazy.layout.flip_down()),
	        Key([mod], "i", lazy.layout.flip_up()),
	        Key([mod], "space", lazy.layout.flip()),


            Key([], "t", lazy.layout.normalize()),
            Key([], "m", lazy.layout.maximize()),
            Key([], "f", lazy.window.toggle_floating()), 
 
            Key([], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
            Key([mod], "Tab", lazy.prev_layout(), desc="Toggle between layouts"),

            ### think of a way to implement the function in the keychords?
            *move_between_groups(groups)

            ], mode=mymodes[0]
        ),

    #applications
    KeyChord([mod], "a", [
            
            Key([mod], "a", lazy.ungrab_chord()),
            
            *launch_apps(myapplications),
            
            *media_keys,
            *basic_stuff,
            
	        ], mode=mymodes[1]
            ),
    KeyChord([mod], "d", [
            Key([mod], "d", lazy.ungrab_chord()),
           
            *browse_the_web(mybrowser, mywebsites),
            
            *media_keys,
            *basic_stuff,

            ], mode=mymodes[2]
        ),
    KeyChord([mod], "f", [ 
            Key([mod], "f", lazy.ungrab_chord()),
           
            *browse_the_web(mysecondbrowser, mywebsites),

            *media_keys,
            *basic_stuff,

            ], mode=mymodes[3]
        ),
    KeyChord([mod], "s", [
            
            Key([mod], "s", lazy.ungrab_chord()),
           
            ], mode= mymodes[4],
        ),
]


for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),
        Key([mod], "u", lazy.screen.prev_group(skip_empty=True)), # cycle left   
        Key([mod], "i", lazy.screen.next_group(skip_empty=True)), #cycle right
    ])

