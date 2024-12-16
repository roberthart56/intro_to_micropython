
#buzz.py
#9/29/24
#buzz

from machine import Pin
import utime

buzz = Pin(3, Pin.OUT)   # create an input pin on pin #1, no pull up resistor

while True:
    for i in range(1000):
        buzz.toggle()
        utime.sleep_us(1000)
        
    for i in range(500):
        buzz.toggle()
        utime.sleep_us(1200)



