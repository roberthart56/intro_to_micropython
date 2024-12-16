#temperature.  Thermistor (~10kOhm at room T).
#prints values 0-65535



from machine import Pin, ADC   #import from machine the classes we need
from time import sleep

volt_adc = ADC(Pin(29))		#name and create the object "volt_adc" to
                                #allow analog to digital conversion on pin.
while True:
    print(volt_adc.read_u16())		#do a 16-bit read (0-65535) on pin.
                                    #and print the result.
    sleep(0.01)
