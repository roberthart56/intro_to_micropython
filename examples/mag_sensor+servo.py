#magnetic field analog input.
#prints values 0-65535

from servo import Servo   #requires that you load servo.py into the microcontroller memory so that its functions can be imported.
from machine import Pin, ADC   #import from machine the classes we need
from time import sleep


my_servo = Servo(pin=1)  #To be changed according to the pin used
my_servo.move(90)  # turns the servo to 0°.

mag_sensor = ADC(Pin(27))		#name and create the object to
                                #allow analog to digital conversion on pin 27
while True:
    value = mag_sensor.read_u16()
    print(value)		#do a 16-bit read (0-65535)
    if value < 1000:
        my_servo.move(0)
        sleep(0.2)
        my_servo.move(90)
    
    

#     time.sleep(1)
#     sg90_servo.move(90)  # turns the servo to 90°.
#     time.sleep(1)
