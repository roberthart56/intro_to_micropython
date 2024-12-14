
#This code blinks two leds on separate pins with independent periods.
#For more LEDs, find ways to scale, perhaps by using a class structure.

from machine import Pin, Timer
led_pin = Pin(0, Pin.OUT)
led_pin_2 = Pin(7, Pin.OUT)

led_timer = Timer()
led_timer_2 = Timer()

def blink(dummy):
    led_pin.toggle()
    
def blink_2(dummy):
    led_pin_2.toggle()
    
led_timer.init(period=500, mode=Timer.PERIODIC, callback=blink)
led_timer_2.init(period=700, mode=Timer.PERIODIC, callback=blink_2)