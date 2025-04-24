#Interrupt with debounce.  4/24/25.  From Chat GPT with editing from Rob Hart.
#LED and resistor to ground on pin 0.  Button between pin 2 and ground.

from machine import Pin
import utime			

# Set up LED and Button
led = Pin(0, Pin.OUT)         # Onboard LED
button = Pin(2, Pin.IN, Pin.PULL_UP)  # External button on GPIO15

# Debounce timing
last_trigger = 0

def handle_interrupt(pin):
    global last_trigger
    now = utime.ticks_ms()
    if utime.ticks_diff(now, last_trigger) > 200:  # 200ms debounce
        led.toggle()
        last_trigger = now

# Attach the interrupt to the button pin
button.irq(trigger=Pin.IRQ_FALLING, handler=handle_interrupt)
