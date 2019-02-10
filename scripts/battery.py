import psutil
import time
import os
battery = psutil.sensors_battery()
while True :
    percent = int(battery.percent)
    is_charging = battery.power_plugged
    if is_charging is False and percent is 15 :
        os.system ("dunstify \"Battery at 15% please connect charger!\"")
    time.sleep(10)