import psutil
import time
import os
battery = psutil.sensors_battery()
while True :
    percent = int(battery.percent)
    is_charging = battery.power_plugged
    if is_charging is False and percent <= 15 :
        os.system ("dunstify \"Battery at " + str(percent) + "% please connect charger!\"")
    time.sleep(10)