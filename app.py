import pifacedigitalio as pfio
from time import sleep

pfio.init()

def turn_on():
    pfio.digital_write(0,1)
    sleep(1)
    pfio.digital_write(0,0)
    
while True:
    turn_on()