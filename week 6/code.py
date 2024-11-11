import os, sys, io
import M5
from M5 import *
import time
import m5utils
from hardware import *

M5.begin()

rgb_strip = RGB(io=5, n=30, type="SK6812")
rgb_strip.fill_color(0xffffff)  
time.sleep_ms(100)

# Configure ADC on pin 1
adc = ADC(Pin(1), atten=ADC.ATTN_11DB)

rgb_timer = time.ticks_ms()  # read current time

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]
colors_counter = 0

# Function to get RGB color as a single integer
def get_rgb_color(r, g, b):
    return (r << 16) | (g << 8) | b

# Cycle through colors on the RGB strip
def color_cycle():
    global rgb_timer
    global colors_counter
    if (time.ticks_ms() > rgb_timer + 400):
        #for r, g, b in colors:
        r, g, b = colors[colors_counter]
        rgb = get_rgb_color(r, g, b)
        rgb_strip.fill_color(rgb)
        #rgb_strip.fill_color(get_rgb_color(r, g, b))
        #time.sleep_ms(400)
        if (colors_counter < len(colors)-1):
            colors_counter += 1
        else:
            colors_counter = 0
        # update timer:
        rgb_timer = time.ticks_ms()

while True:
    M5.update()
    
    # Read ADC value and map it to range 0-255
    adc_val = int(m5utils.remap(adc.read(), 0, 4095, 0, 255))
    
    # Conditional color change based on ADC value
    if adc_val < 90:
        color_cycle()
        
    else:
        rgb_strip.fill_color(0xffffff)
    
    # Print ADC value
    print(adc_val)
    
    # Delay to prevent data overload
    time.sleep_ms(50)
