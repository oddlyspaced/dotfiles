import psutil
import time
import os
import socket 
import getpass
import datetime
import subprocess

battery = psutil.sensors_battery()
percent = int(battery.percent)
is_charging = battery.power_plugged
current_date_time = datetime.datetime.now()

username = str(getpass.getuser())
hostname = str(socket.gethostname())
time = (current_date_time.strftime("%I:%M:%S %p"))

username_string = username + "@" + hostname
time_string = "Time : " + str(time)
battery_level_string = "Battery : " + str(percent)
battery_charging_string = "Is Charging : " + str(is_charging)

side_spaces = int(15)

username = (" " * (side_spaces - len(username))) + username
hostname = hostname +  (" " * (side_spaces - len(hostname)))
time_prefix = "Time "
time_prefix = (" " * (side_spaces - len(time_prefix))) + time_prefix
time_suffix = " " + time
time_suffix = time_suffix + (" " * (side_spaces - len(time_suffix)))
time = time_prefix + ":" + time_suffix
battery_prefix = "Battery "
battery_prefix = (" " * (side_spaces - len(battery_prefix))) + battery_prefix
battery_suffix = " " + str(percent) + "%"
if is_charging :
    battery_suffix = battery_suffix + " ~"
battery_suffix = battery_suffix + (" " * (side_spaces - len(battery_suffix)))
battery_string = battery_prefix + ":" + battery_suffix
wifi_prefix = "Wifi "
wifi_prefix = (" " * (side_spaces - len(wifi_prefix))) + wifi_prefix
wifi_suffix = str(subprocess.check_output ("bash get_wifi.sh", shell = True)).strip()[2:-3]
if len(wifi_suffix) == 0 :
    wifi_suffix = "Not Connected"
wifi_suffix = " " + wifi_suffix
wifi_suffix = wifi_suffix + (" " * (side_spaces - len(wifi_suffix)))
wifi_string = wifi_prefix + ":" + wifi_suffix

message = username + "@" + hostname + "\n" + time + "\n" + battery_string + "\n" + wifi_string
os.system ("dunstify " + "\"" + message + "\"")