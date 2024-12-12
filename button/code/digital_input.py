from machine import Pin
from time import sleep
light_detector = Pin(26, Pin.IN, Pin.PULL_UP)

while True:
    print(light_detector.value())
    sleep(0.1)