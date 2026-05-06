
import machine
from neopixel import NeoPixel
from time import sleep

Num_pix = 5

pixels = NeoPixel(machine.Pin(1), Num_pix)  #set up Pixel array

colors  = [(10,0,0),(0,10,0),(0,0,10),(10,10,10),(0,0,0)]  #create a list of colors. Maximum is 255

while True:
        for j in range(Num_pix):
            for i in range(Num_pix):
              pixels[i] = colors[(i+j) % Num_pix]  #assign colors to
            pixels.write()
            sleep(.5)

