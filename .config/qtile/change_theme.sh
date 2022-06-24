#!/bin/sh

# backend for pywal: wal, haishoku, colorz
#this script aims to change the wallpaper with pywal, then refresh all themes
wal -i ~/Pictures/Wallpapers/ --backend colorz & 
sleep 0.25  
qtile cmd-obj -o cmd -f restart &
kitty -e xrdb /home/bastien/.Xresources
kitty -e spicetify apply  
bash ~/.config/dunst/launch_dunst.sh
