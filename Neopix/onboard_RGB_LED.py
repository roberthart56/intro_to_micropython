import machine
import neopixel
import time

# Define the GPIO pin connected to the onboard RGB LED (D7 or GPIO25 for Xiao RP2040)
LED_PIN = 12  # Check the Xiao RP2040 pinout to confirm
NUM_PIXELS = 1  # There's only one onboard RGB LED

power = machine.Pin(11,machine.Pin.OUT)
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
