import subprocess
# getting id of device
device_tags = ["ELAN", "Touchpad"]
devices = list(subprocess.getoutput("xinput list").split("\n"))

id = -1

for st in devices:
    tag_count = 0
    for tag in device_tags:
        if tag in str(st):
            tag_count = tag_count + 1
    if tag_count == len(device_tags):
        for sub in st.split("\t"):
            if "id=" in sub:
                id = int(sub[3:])

prop_tags = ["Tapping", "Enabled"]
properties = list(subprocess.getoutput("xinput list-props " + str(id)).split("\n"))

prop = -1
flag = 0
for st in properties:
    if flag == 1:
        break
    tag_count = 0
    for tag in prop_tags:
        if tag in str(st):
            tag_count = tag_count + 1
    if tag_count == len(prop_tags):
        for sub in st.split(" "):
            if "(" in sub:
                prop = int(sub[1:4])
                print(prop)
                flag = 1

subprocess.getoutput("xinput set-prop " + str(id) + " " + str(prop) + " 1")