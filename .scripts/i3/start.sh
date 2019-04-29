#!/bin/bash
# Script to run commands on i3 start
nitrogen --restore
pulseaudio &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
sleep 1 &
nm-applet &
compton -b &
~/.scripts/conky/start.sh &
~/.scripts/i3/refesh.sh &
exit 0
