#!/bin/sh
# launcher.sh
# navigate to pi-wol, then starts the client
cd /
cd /home/pi/pi-wol
sudo python3 mqtt_daemon.py
cd /