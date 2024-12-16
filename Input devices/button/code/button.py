#button.py
#9/29/24
#detect and print button state.

from machine import Pin
import time

button = Pin(3, Pin.IN, Pin.PULL_UP)



while True:
    print(button.value())
    time.sleep(0.1)



