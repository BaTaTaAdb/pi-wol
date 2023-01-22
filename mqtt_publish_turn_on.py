# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish

publish.single("BaTaTaAdb/test", "Hello", hostname="test.mosquitto.org")
publish.single("BaTaTaAdb/pc", "World!", hostname="test.mosquitto.org")
print("Done")
 