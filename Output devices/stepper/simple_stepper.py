#simple_stepper.py
#3/2/26 add comments.
#Program for use with modular thing stepper:
#see https://github.com/modular-things/modular-things/tree/main/things/stepper-hbridge-xiao/circuit
#stepper code for two TB67H452FTG dual h bridge chips.
#and RP2040 XIAO.
#VREF is generated via PWM through an RC Filters, or set to max by turning the refernce pins on.  
# 





from machine import Pin, PWM
from time import sleep

# ----------code block below used to set up PWM on pins 27 and 29 to generated ref. voltage for current control------

# pwma = PWM(Pin(27), freq=500000, duty_u16=32768)  # vref for A
# pwmb = PWM(Pin(29), freq=500000, duty_u16=32768)   #vref for B
# 
# pwma.duty_u16(2100) #with .3 mOhm Sense Resistor, I = V/3
# pwmb.duty_u16(2400)


# ----------code block below used to set vref at 3V so that current is not limited for 30 Ohm coil R and 3.3V.

REF_A = Pin(27, Pin.OUT)	
REF_B = Pin(29, Pin.OUT)

REF_A.on()
REF_B.on()

# ----------set up stepper pins.

A1_in = Pin(6, Pin.OUT)
A2_in = Pin(7, Pin.OUT)
B1_in = Pin(28, Pin.OUT)
B2_in = Pin(4, Pin.OUT)

#------function definitions ------

def stepper_off():
    A1_in.off()
    A2_in.off()
    B1_in.off()
    B2_in.off()


def step(n):
    if n == 0:
        A1_in.on()
        A2_in.off()
        B1_in.on()
        B2_in.off()
    
    elif n == 1:
        A1_in.on()
        A2_in.off()
        B1_in.off()
        B2_in.on()
        
    elif n == 2:
        A1_in.off()
        A2_in.on()
        B1_in.off()
        B2_in.on()
        
    else:
        A1_in.off()
        A2_in.on()
        B1_in.on()
        B2_in.off()


def main():
    while True:
        for i in range(4):
            step(i)
            #print(i)
            sleep(0.1)
        

if __name__ == "__main__":

    main()