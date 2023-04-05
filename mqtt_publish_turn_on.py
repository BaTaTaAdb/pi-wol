# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish
from time import sleep

sleep(1)
publish.single("BaTaTaAdb/pc", "neon_on", hostname="test.mosquitto.org")
sleep(2)
publish.single("BaTaTaAdb/pc", "neon_off", hostname="test.mosquitto.org")
print("Done")
 