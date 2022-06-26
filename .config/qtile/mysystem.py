######################################
## ____            _                 #
##/ ___| _   _ ___| |_ ___ _ __ ___  #
##\___ \| | | / __| __/ _ \ '_ ` _ \ #
## ___) | |_| \__ \ ||  __/ | | | | |#
##|____/ \__, |___/\__\___|_| |_| |_|#
##       |___/                       ##########
##__     __         _       _     _           #
##\ \   / /_ _ _ __(_) __ _| |__ | | ___  ___ #
## \ \ / / _` | '__| |/ _` | '_ \| |/ _ \/ __|#
##  \ V / (_| | |  | | (_| | |_) | |  __/\__ \#
##   \_/ \__,_|_|  |_|\__,_|_.__/|_|\___||___/# 
###############################################


#write apps-name as a launch command (for example "spotify --minimized")
## the dictionary keys are used to generate the keybindings
## through use of modes and keychords, keybinds for applications, websites or 
## groups don't overlap 
## "a" is reserved for app mod, b for browser und f second browser aka firefox
## appearance now source this but use the keys here (myapplications["h"]. Changing
## the keybindings mean changing the values in appearance.py


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
   "h" : "kitty -e htop",                        
   "t" : "kitty -e bpytop", 
   "g" : "gimp",
   "r" : "kitty -e ranger",
   "j" : "kitty -e conda run jupyter-notebook",
   "XF86AudioLowerVolume" : "kitty -e pulsemixer",
   "XF86AudioRaiseVolume" : "kitty -e alsamixer"
        }

mywebsites = {
    "y" : "www.youtube.com",
    "w" : "www.wikipedia.com",
    "g" : "https://wiki.gentoo.org/",
    "a" : "www.wiki.archlinux.org",
    "l" : "www.gitlab.com",
    "h" : "www.github.com",
    "t" : "https://intranet.ulb.tu-darmstadt.de",
    "k" : "https://kvk.bibliothek.kit.edu/?digitalOnly=0&embedFulltitle=0&newTab=0",
    "u" : "https://www.ulb.tu-darmstadt.de/die_bibliothek/index.de.jsp",
    
    "m" : "https://www.francetabs.com/tablatures-partitions/nouvelles-tabs-guitare.html",
    "n" :  "https://www.ultimate-guitar.com/",
    "b" : "https://www.boiteachansons.net/",
    "c" : "https://www.cifraclub.com/",
     
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

