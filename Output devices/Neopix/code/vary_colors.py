
import machine
from neopixel import NeoPixel
from time import sleep

Num_pix = 30

pixels = NeoPixel(machine.Pin(1), Num_pix)  #set up Pixel array

for i in range(Num_pix):
    pixels[i] = (0,0,0)  

pixels.write()
sleep(0.5)


for i in range(Num_pix):
    pixels[i] = (30-i,i,0)
    
pixels.write()



