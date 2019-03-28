#!/bin/bash

echo "Installing packages..."
sudo pacman -S conky termite nitrogen papirus-icon-theme scrot xorg-xbacklight
yay -S polybar compton-tryone-git ttf-comfortaa nerd-fonts-ubuntu-mono ttf-google-sans ant-dracula-gtk-theme i3lock-fancy-git pulseaudio-ctl
nitrogen --set-zoom-fill wallpaper.jpg

echo "Setting configs..."
cp -r .config/compton.conf ~/.config/
cp -r .config/conky/ ~/.config/
cp -r .config/i3/ ~/.config/
cp -r .config/polybar/ ~/.config/
cp -r .config/termite/ ~/.config/

echo "All Done!\nPlease go ahead and use lxappearance to set gtk theme to Ant Dracula. Also replace wlo1 with your wifi interface in polybar config"