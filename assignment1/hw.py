import os, sys, io
import M5
from M5 import *
from hardware import *
import time

print('digital input to change RGB colors')


M5.begin()


rgb_strip = RGB(io=2, n=10, type="SK6812")


rgb_strip.fill_color(0xff0000)  
time.sleep_ms(100)  


input_pin = Pin(7, mode=Pin.IN, pull=Pin.PULL_UP)

def get_rgb_color(r, g, b):
    rgb_color = (r << 16) | (g << 8) | b
    return rgb_color


def color_cycle():
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]
    for r, g, b in colors:
        rgb_strip.fill_color(get_rgb_color(r, g, b))
        time.sleep_ms(500)  

while True:
    M5.update()  

    if input_pin.value() == True:  
        print('Pin 7 is HIGH, setting color to RED')
        rgb_strip.fill_color(0xff0000)  
    else:  
        print('Pin 7 is LOW, cycling through colors')
        color_cycle()

    time.sleep_ms(100)  

