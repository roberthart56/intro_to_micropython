#button_conditional.py
#5/5/26
#detect and print button state.

from machine import Pin
import time

button = Pin(1, Pin.IN, Pin.PULL_UP)



while True:
    if button.value():
        print("button up")
    else:
        print("button down")
        
    time.sleep(0.1)




