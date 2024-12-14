#magnetic field analog input.
#prints values 0-65535



from machine import Pin, ADC   #import from machine the classes we need
from time import sleep

mag_sensor = ADC(Pin(27))		#name and create the object to
N = 100000                              #allow analog to digital conversion on pin 27

while True:
    ave=0
    for _ in range(N):
        ave = ave + mag_sensor.read_u16()		#do a 16-bit read (0-65535)
        
    print(ave/N)

