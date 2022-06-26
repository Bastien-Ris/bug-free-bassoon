#! /usr/bin/bash

# Volume notification: Pulseaudio and dunst
# inspired by gist.github.com/sebastiencs/5d7227f388d93374cebdf72e783fbd6a
# inspired by Chanasit/pulse-audio-notify.sh
# inspired by arch linux wiki


icon_path=/usr/share/icons/HighContrast/48x48/status/
notify_id=506
sink_nr=0   # use `pacmd list-sinks` to find out sink_nr
# Arbitrary but unique message tag
msgTag="myvolume"

function get_volume {
    pacmd list-sinks | awk '/\tvolume:/ { print $5 }' | tail -n+$((sink_nr+1)) | head -n1  | cut -d '%' -f 1
}

function get_volume_icon {
    if [ "$1" -lt 34 ]
    then
        echo -n "audio-volume-low.png"
    elif [ "$1" -lt 67 ]
    then
        echo -n "audio-volume-medium.png"
    else   
        echo -n "audio-volume-high.png"
    fi
}

function volume_notification {
    volume=`get_volume`
    vol_icon=`get_volume_icon $volume`
    bar=$(seq -s "─" $(($volume / 5)) | sed 's/[0-9]//g')
    dunstify -r $notify_id -u low -i $icon_path$vol_icon  -h string:x-dunst-stack-tag:$msgTag "Volume: ${volume}%" \
    -h int:value:"$volume" "Volume: ${volume}%"
}

function mute_notification {
    volume=`get_volume`
    muted=$(pacmd list-sinks | awk '/muted/ { print $2 }' | tail -n+$((sink_nr+1)) | head -n1)
    if [ $muted == 'yes' ]
    then
        dunstify -r $notify_id -u low -i ${icon_path}audio-volume-muted.png mute -h string:x-dunst-stack-tag:$msgTag "Volume muted"
    else
        dunstify -r $notify_id -u low -i ${icon_path}`get_volume_icon $(get_volume)` unmute -h string:x-dunst-stack-tag:$msgTag "Volume unmuted" \  -h int:value:"$volume" "Volume: ${volume}%"
    fi
}
case $1 in
  up)
      pactl set-sink-volume $sink_nr +5%
      volume_notification
      ;;
  up+)
      pactl set-sink-volume $sink_nr +20%
      volume_notification
      ;;
  down)
      pactl set-sink-volume $sink_nr -5%
      volume_notification
    ;;
  down+)
      pactl set-sink-volume $sink_nr -20%
      volume_notification
    ;;
  mute)
      pactl set-sink-mute $sink_nr toggle
      mute_notification
      ;;
  *)
      echo "Usage: $0 up | up + | down | down + | mute"
      ;;
esac
