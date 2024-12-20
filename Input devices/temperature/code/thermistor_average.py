#temperature.  Thermistor (~10kOhm at room T).
#prints values 0-65535



from machine import Pin, ADC   #import from machine the classes we need
from time import sleep

volt_adc = ADC(Pin(29))		#name and create the object "volt_adc" to allow analog to digital conversion on pin 26
avg = 0
Numspls = 10000

while True:
    for _ in range(Numspls):
        avg = avg + volt_adc.read_u16()		#do a 16-bit read (0-65535) on pin 26
    print(avg/Numspls)
    avg = 0
    