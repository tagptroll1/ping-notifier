import re
import time
import subprocess
from winsound import PlaySound, SND_FILENAME

import netifaces
from plyer import notification

gws = netifaces.gateways()
router_ip = gws["default"][netifaces.AF_INET][0]

regex = re.compile(r"time=(\d+)ms")

while True:
    resp = subprocess.Popen(
        f'ping -n 1 {router_ip} | FIND "time="', 
        stdout=subprocess.PIPE, 
        text=True,
        shell=True
    )
    out, err = resp.communicate()
    
    match = regex.search(out)
    ms_time = match.group(1)

    print("Current ping: ", ms_time)

    if int(ms_time) > 1:
        notification.notify()
        PlaySound("wah.wav", SND_FILENAME)
        time.sleep(60)
    time.sleep(5)