#!/bin/sh


# the restart is to sync with wal  
# xrandr --rate 75 &
# xset s off -dpms &&
xautolock -time 20 -locker slimlock -notify 120 -notifier dunst -killtime 120 -killer "sudo -P shutdown" &
wal -R &
picom -b &
redshift &
clipmenud &
pcmanfm -d &
#volumeicon &
#birdtray &
#spotify --minimized  &
#.config/qtile/change_theme.sh
