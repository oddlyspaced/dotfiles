#!/bin/bash
cd ~/.config/conky
killall -p conky
conky -c info
exit 0
