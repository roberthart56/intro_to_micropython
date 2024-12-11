#light detection as analog input.
#prints values 0-65535



from machine import Pin, ADC   #import from machine the classes we need
from time import sleep

light_adc = ADC(Pin(26))		#name and create the object "light_adc" to
                                #allow analog to digital conversion on pin 26
while True:
    print(light_adc.read_u16())		#do a 16-bit read (0-65535) on pin 26
                                    #and print the result.
    sleep(0.01)