#digital_io.py
#9/29/24
#detect and print button state.

from machine import Pin
import time

led = Pin(0, Pin.OUT)  
led.off()
button = Pin(1, Pin.IN, Pin.PULL_UP)



while True:
    #print(button.value())    
    if button.value() == 0:
        led.on()
    else:
        led.off()
        
    time.sleep(0.1)


