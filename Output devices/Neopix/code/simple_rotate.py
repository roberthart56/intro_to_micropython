
import machine
from neopixel import NeoPixel
from time import sleep

Num_pix = 5

pixels = NeoPixel(machine.Pin(1), Num_pix)  #set up Pixel array

colors  = [(10,0,0),(0,10,0),(0,0,10),(10,10,10),(0,0,0)]  #create a list of colors. Maximum is 255

while True:
    # send current colors to LEDs
    for i in range(Num_pix):
        pixels[i] = colors[i]
    pixels.write()
    sleep(0.5)

    # rotate the list (move last item to the front)
    last = colors[-1]        # save last color
    for i in range(Num_pix - 1, 0, -1):
        colors[i] = colors[i - 1]
    colors[0] = last