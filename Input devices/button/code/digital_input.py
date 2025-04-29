#digital input, with button.  Button attached to an I/O pin, number 26 in this case.

from machine import Pin
from time import sleep

button = Pin(26, Pin.IN, Pin.PULL_UP)

while True:
    print(button.value())
    sleep(0.1)
