#code suggested by Chat GPT, and modified to work by R. Hart, 2024.
#blinks the RGB LED on the XIAO RP2040 board.

import machine
import neopixel
import time


LED_PIN = 12  # Check the Xiao RP2040 pinout to confirm
NUM_PIXELS = 1  # There's only one onboard RGB LED

power = machine.Pin(11,machine.Pin.OUT)  #This provides power for the RGB LED.
power.value(1)

# Initialize the NeoPixel object
np = neopixel.NeoPixel(machine.Pin(LED_PIN), NUM_PIXELS)

# Function to set the LED color
def set_color(red, green, blue):
    np[0] = (red, green, blue)  # Set RGB values (0-255)
    np.write()  # Update the LED

# Example: Cycle through red, green, and blue
try:
    while True:
        set_color(255, 0, 0)  # Red
        time.sleep(1)
        set_color(0, 255, 0)  # Green
        time.sleep(1)
        set_color(0, 0, 255)  # Blue
        time.sleep(1)
except KeyboardInterrupt:
    set_color(0, 0, 0)  # Turn off the LED
