import time
from machine import Pin, SoftI2C
import ssd1306  #install this using Thonny, for example.
import math

#Pin assignment
i2c = SoftI2C(scl=Pin(7), sda=Pin(6))  # Adjust the Pin numbers based on your connections
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
variable=3.14
oled.fill(0)  # Clear the screen
oled.text("Hello World", 10, 15)
oled.text(str(variable), 10, 25)
oled.show()  # Show the text