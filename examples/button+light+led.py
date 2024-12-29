from machine import Pin
from time import sleep

'''
button on:0
led on:7
photo_sensor on:2
'''

'''
button needs input pullup.
pressing button brings input to ground.
'''
button = Pin(0, Pin.IN, Pin.PULL_UP)

led = Pin(7, Pin.OUT) #Set up led as output.

'''
# phototransistor has 100k resistor to ground.
Input goes to zero when light is blocked.
'''
photo_sensor = Pin(2, Pin.IN)  

while True:
    if not photo_sensor.value() and not button.value():
        led.value(1)
    else:
        led.value(0)

    sleep(0.2)
    
    print('light = ',photo_sensor.value(),'  button = ', button.value())