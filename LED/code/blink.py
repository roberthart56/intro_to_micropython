#This is a comment!  Does not get interpreted by python.

#blink.py 

from machine import Pin  #this library has classes and functions that deal with microcontrollers.
import time		#library to handle time functions.

#An LED is attached to pin 7 of the xiao RP2040 module.

#led_1 is created as an instance of the Class 'Pin'.  The first argument is the pin
#number.  The second argument sets the function of the pin.
led_1 = Pin(0, Pin.OUT)   

while True:					#loop forever
    led_1.value(1)			#make the voltage on the pin high.
    time.sleep(1.0)			#sleep for a second
    led_1.value(0)			#make the voltage on the pin low.
    time.sleep(1.0)			#sleep for another second
