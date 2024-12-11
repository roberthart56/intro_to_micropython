#digital_io.py
#9/29/24
#detect and print button state.

from machine import Pin
import time

button = Pin(26, Pin.IN)



while True:
    print(button.value())
    time.sleep(0.1)



