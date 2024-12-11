
import machine
from neopixel import NeoPixel
from time import sleep

Num_pix = 4

pixels = NeoPixel(machine.Pin(2), Num_pix)  #set up Pixel array

colors  = [(100,100,0),(0,100,0),(0,0,100),(100,100,100)]

for i in range(Num_pix):
    pixels[i] = colors[i]  #maximum is 511

pixels.write()

