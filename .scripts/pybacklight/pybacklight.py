#!/bin/python3
import subprocess
import sys
from os import listdir
def parse_arg() :
    args = list(sys.argv)
    args.remove(args[0]) # removing script call
    if len(args) > 0 :
        for arg in args :
            try :
                arg_copy = str(arg)
                arg = int(arg) # this serves as the test case
                set_backlight(arg_copy)
                break
            except :
                print_help()
                quit()
    else :
        print_help()

def set_backlight(brightness) :
    card = get_card()
    current_brightness = int(str(subprocess.check_output("cat /sys/class/backlight/" + card + "/brightness", shell=True))[2:-3])
    brightness = str(brightness)
    if (brightness.startswith("+") or brightness.startswith("-")) :
        brightness = current_brightness + int(brightness)
        if brightness < 0 :
            brightness = 0
        if brightness > get_max_brightness() :
            brightness = get_max_brightness()
    command = str("echo \"" + str(brightness) + "\" > /sys/class/backlight/" + str(card) + "/brightness")
    subprocess.call(command, shell=True, executable='/bin/bash')

# get card returns the first instance of the card it finds
def get_card() :
    return str(list(listdir("/sys/class/backlight"))[0])

def get_max_brightness() :
    return int(str(subprocess.check_output("cat /sys/class/backlight/" + get_card() + "/max_brightness", shell=True))[2:-3])

def print_help() :
    print("Usage: <pybacklight> <value>")
    print("pybacklight -<value>  -> Decreases brightness by <value>")
    print("Example: pybacklight -5        -> Will decreases brightness by 5")
    print("pybacklight +<value>  -> Increases brightness by <value>")
    print("Example: pybacklight +5        -> Will increase brightness by 5")
    print("pybacklight <value>   -> Will set <value> as brightness")
    print("Example: pybacklight 100  -> Will set brightness to 100 points")

parse_arg()