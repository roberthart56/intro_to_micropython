
import machine
from neopixel import NeoPixel
from time import sleep

Num_pix = 30

pixels = NeoPixel(machine.Pin(1), Num_pix)  #set up Pixel array

pixels.write()

sleep(1)

for i in range(Num_pix):
    pixels[i] = (50,0,50)
    
while True:    
pixels.write()



