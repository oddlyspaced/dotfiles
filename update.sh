#!/bin/bash
mkdir -p ~/.config/i3
cp i3-config ~/.config/i3/config
mkdir -p ~/.config/termite
cp termite-config ~/.config/termite/config
cp compton-config ~/.config/compton.conf
mkdir -p ~/.config/polybar
cp polybar-config ~/.config/polybar/config
cp polybar-launch.sh ~/.config/polybar/launch.sh
mkdir -p ~/.config/dunst
cp dunst-config ~/.config/dunst/dunstrc
mkdir -p ~/.config/rofi
cp rofi-config ~/.config/rofi/config
mkdir -p ~/.config/conky
cp conky-info ~/.config/conky/info
cp conky-start.sh ~/.config/conky/start.sh
