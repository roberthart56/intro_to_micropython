# write_ADC.py collects and saves data to device file.
#9/30/24

import os
import machine
import time

data_length = 20
adc = machine.ADC(26)            # create ADC object on ADC pin
data = []

for i in range(data_length):
    d=adc.read_u16()  # read a raw analog value in the range 0-65535       
    volts = d*3.3/65535
    print(volts)
    data.append(volts)
    time.sleep(0.1)
   
# Open the file in write mode
with open("example.txt", "w") as file:
    for element in data:
        file.write(str(element)+"\n")
    file.close()





