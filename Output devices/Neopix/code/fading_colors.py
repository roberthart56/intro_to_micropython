
import machine
from neopixel import NeoPixel
from time import sleep

Num_pix = 30

pixels = NeoPixel(machine.Pin(1), Num_pix)  #set up Pixel array

colors = [(0,0,0)]*Num_pix

for i in range(Num_pix):		#initialize colors
    colors[i] = (30-i,i,0)
    
while True:

    for i in range(Num_pix):
        pixels[i] = colors[i]
        
    for i in range(Num_pix):
        colors[i] = pixels[i][0]+1,pixels[i][1]-2,pixels[i][2]+3
        
        
    pixels.write()

    sleep(0.1)

