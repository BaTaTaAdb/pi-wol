import pifacedigitalio as pfio
from time import sleep




def turn_on():
    pfio.init()
    pfio.digital_write(0,0)
    pfio.digital_write(0,1)
    sleep(0.1)
    pfio.digital_write(0,0)

"""while True:
    turn_on()"""
