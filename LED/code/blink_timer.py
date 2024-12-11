from machine import Pin, Timer
led_pin = Pin(0, Pin.OUT)

led_timer = Timer()

def blink(dummy):
    led_pin.toggle()
    

    
led_timer.init(period=500, mode=Timer.PERIODIC, callback=blink)
