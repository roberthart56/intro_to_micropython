from oled_numbers import draw_number
from machine import Pin, SoftI2C
import ssd1306
import time


i2c = SoftI2C(scl=Pin(7), sda=Pin(6))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

draw_number(oled, 5000)   #passing the oled object as a function argument

count = 0

while True:
    draw_number(oled, count)
    count += 1
    time.sleep(0.2)