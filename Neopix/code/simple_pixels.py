
import machine
from neopixel import NeoPixel
from time import sleep

Num_pix = 4

pixels = NeoPixel(machine.Pin(1), Num_pix)  #set up Pixel array

colors  = [(100,0,0),(0,100,0),(0,0,100),(100,100,100)]  #create a list of colors. Maximum is 255

for i in range(Num_pix):
    pixels[i] = colors[i]  #assign colors to

pixels.write()

