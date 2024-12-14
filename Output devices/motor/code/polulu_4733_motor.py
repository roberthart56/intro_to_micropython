#This is a comment!  Does not get interpreted by python.

#polulu_4733_motor.py see circuit for this driver online at polulu.com

from machine import Pin  #this library has classes and functions that deal with microcontrollers.
import time		#library to handle time functions.


m1 = Pin(4, Pin.OUT)
m2 = Pin(2, Pin.OUT)   

m1.off()
m2.on()
time.sleep(2)
m2.off()
time.sleep(1)
m1.on()

