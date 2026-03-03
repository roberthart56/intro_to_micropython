from machine import Pin, PWM
from time import sleep
from math import sin, cos, pi

amp_a = 2100
amp_b = 2400

N= 16   #divisions of step

pwma = PWM(Pin(27), freq=500000, duty_u16=32768)  # vref for A
pwmb = PWM(Pin(29), freq=500000, duty_u16=32768)   #vref for B

pwma.duty_u16(amp_a) #with .3 mOhm Sense Resistor, I = V/3
pwmb.duty_u16(amp_b)

# REF_A = Pin(27, Pin.OUT)	#for 30 Ohm phase and 5V supply, set current to max.
# REF_B = Pin(29, Pin.OUT)


A1_in = Pin(6, Pin.OUT)
A2_in = Pin(7, Pin.OUT)
B1_in = Pin(28, Pin.OUT)
B2_in = Pin(4, Pin.OUT)

# REF_A.on()
# REF_B.on()

def sin_step(n):
    
    duty_a = int(sin(n*pi/(2*N))*amp_a)
    duty_b = int(cos(n*pi/(2*N))*amp_b)
    
    if duty_a < 0:
        duty_a = -duty_a
        A1_in.off()
        A2_in.on()
        pwma.duty_u16(duty_a)
        
    else:
        A2_in.off()
        A1_in.on()
        pwma.duty_u16(duty_a)
        
    if duty_b < 0:
        duty_b = -duty_b
        B1_in.off()
        B2_in.on()
        pwmb.duty_u16(duty_b)
        
    else:
        B2_in.off()
        B1_in.on()
        pwmb.duty_u16(duty_b)
    #print(duty_a, duty_b)


def main():
    while True:
        for i in range(4*N):
            sin_step(i)
            #print(i)
            sleep(1/N)  #for 2*pi/200 rotation per second.
        
if __name__ == "__main__":

    main()