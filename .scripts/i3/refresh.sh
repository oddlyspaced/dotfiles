#!/bin/bash
~/.scripts/polybar/launch.sh
killall -p compton
compton -b &
