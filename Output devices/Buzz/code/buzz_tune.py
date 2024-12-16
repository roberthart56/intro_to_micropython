
#buzz.py
#9/29/24
#buzz

from machine import Pin
import utime

buzz = Pin(3, Pin.OUT)   # create an input pin on pin #1, no pull up resistor

half_period = (1000,1200,800,600,900)
duration = (1000,500,230,1000,750)

while True:
    for i in range(5):
        for j in range(duration[i]):
            buzz.toggle()
            utime.sleep_us(half_period[i])
        
    




