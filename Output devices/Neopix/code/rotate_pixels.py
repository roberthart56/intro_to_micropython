
import machine
from neopixel import NeoPixel
from time import sleep

Num_pix = 4

pixels = NeoPixel(machine.Pin(1), Num_pix)  #set up Pixel array

colors  = [(255,0,0),(0,255,0),(0,0,255),(100,100,100)]

j=0

while True:
    for i in range(Num_pix):
        pixels[(i+j)%4] = colors[i]  #maximum is 511
        pixels.write()
    j=j+1
    sleep(0.1)
    
