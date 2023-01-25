# MQTT Client demo
# Continuously monitor two different MQTT topics for data,
# check if the received data matches two predefined 'commands'
import paho.mqtt.client as mqtt
import pifacedigitalio as pfio
import paho.mqtt.publish as publish
from time import sleep
#from daemonize import Daemonize

class Instance():
    
    def __init__(self, pc_is_on) -> None:
        self.pc_is_on = pc_is_on
        pfio.init()
        pfio.digital_write(0,0)
    
    def turn_on():
        pfio.digital_write(0,1)
        sleep(0.4)
        pfio.digital_write(0,0)
    
        
    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
    
        # Subscribing in on_connect() - if we lose the connection and
        # reconnect then subscriptions will be renewed.
        
        #client.subscribe("BaTaTaAdb/test")
        client.subscribe("BaTaTaAdb/pc")
        client.subscribe("BaTaTaAdb/ping")
    
    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))

        if msg.payload == b"turn_on":
            print("Turning on computer!")
            if not self.pc_is_on:
                self.turn_on()
                self.pc_is_on = True
            else:
                print("Already on!")

        if msg.payload == b"turn_off":
            print("Turning off computer!")
            if self.pc_is_on:
                self.turn_on()
                self.pc_is_on = False
            else:
                print("Already off!")
                
        if msg.payload == b"ping":
            print("Pong!")
            publish.single("BaTaTaAdb/pc", "Pong!", hostname="test.mosquitto.org")

        
        client.connect("test.mosquitto.org", 1883, 60)

        # Process network traffic and dispatch callbacks. This will also handle
        # reconnecting. Check the documentation at
        # https://github.com/eclipse/paho.mqtt.python
        # for information on how to use other loop*() functions
        client.loop_forever()

def main():
    instance = Instance(True)
    # Create an MQTT client and attach our routines to it.
    client = mqtt.Client()
    client.on_connect = instance.on_connect
    client.on_message = instance.on_message 

while True:
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting")
        exit(0)
    except Exception as e:
        print(e)
