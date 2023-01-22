import pifacedigitalio as pfio
from time import sleep

pfio.init()

def turn_on():
    pfio.digital_write(0,1)
    sleep(0.2)
    pfio.digital_write(0,0)
    sleep(0.2)
    pfio.digital_write(1,1)
    sleep(0.2)
    pfio.digital_write(1,0)
    sleep(0.2)

while True:
    turn_on()
