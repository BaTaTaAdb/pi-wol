# MQTT Client demo
# Continuously monitor two different MQTT topics for data,
# check if the received data matches two predefined 'commands'
import paho.mqtt.client as mqtt
import pifacedigitalio as pfio
from time import sleep
#from daemonize import Daemonize
from sys import argv

pfio.init()
pfio.digital_write(0,0)
pfio.digital_write(1,1)
sleep(0.4)
pfio.digital_write(1,0)
pc_is_on = bool(argv[1]) if len(argv) > 1 else False

def switch_pc(state):
    if state == "on" and pc_is_on:
        print("Already on!")
        return
    if state == "off" and not pc_is_on:
        print("Already off!")
        return
    if state == "switch":
        pass
    pfio.digital_write(0,1)
    sleep(0.4)
    pfio.digital_write(0,0)
    print(f"Turning {state} computer!")
    
def neon(on: bool):
    pfio.digital_write(1,int(on))
    

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    
    #client.subscribe("BaTaTaAdb/test")
    client.subscribe("BaTaTaAdb/pc")
    #client.subscribe()
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    if msg.payload == b"turn_on":
        #print("Turning on computer!")
        switch_pc("on")

    elif msg.payload == b"turn_off":
        #print("Turning off computer!")
        switch_pc("off")
            
    elif msg.payload == b"ping":
        print("pong")
        
    elif msg.payload == b"switch":
        switch_pc("switch")
        
    elif msg.payload == b"neon_on":
        neon(True)
        
    elif msg.payload == b"neon_off":
        neon(False)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

# Process network traffic and dispatch callbacks. This will also handle
# reconnecting. Check the documentation at
# https://github.com/eclipse/paho.mqtt.python
# for information on how to use other loop*() functions
client.loop_forever()
