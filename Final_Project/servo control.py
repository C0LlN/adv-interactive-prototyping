import os, sys, io
import M5
from M5 import *
from hardware import *
import time
from machine import Pin, PWM


M5.begin()


pwm1 = PWM(Pin(38))


pwm1.freq(50)


duty_cycle = 0  
pwm1.duty(duty_cycle)


button = Pin(8, Pin.IN, Pin.PULL_UP)  

current_state = 0  
previous_button_state = 1  


while True:
    M5.update()  

    
    button_state = button.value()

    
    if previous_button_state == 1 and button_state == 0:
        if current_state == 0:
            
            print("Button pressed: Setting duty cycle to 65.")
            pwm1.duty(69)
            time.sleep(2)  
            print("Stopping servo.")
            pwm1.duty(0)  
            current_state = 1  
        elif current_state == 1:
            
            print("Button pressed: Setting duty cycle to 85.")
            pwm1.duty(85)
            time.sleep(2)  
            print("Stopping servo.")
            pwm1.duty(0)  
            current_state = 0  

    
    previous_button_state = button_state

    
    time.sleep(0.1)
