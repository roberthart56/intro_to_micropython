#digital_io.py
#9/29/24
#detect and print button state.

from machine import Pin
import time

led = Pin(1, Pin.OUT)  

button = Pin(3, Pin.IN, Pin.PULL_UP)



while True:
    led.value(not(button.value()))
    print(button.value())
    time.sleep(0.1)



