# read ADC and button inputs and print values separated by comma
# use this code to test webserial_pyscript_template

import os, sys, io
import M5
from M5 import *
import time
import m5utils
from hardware import *




button1 = Pin(1, mode=Pin.IN, pull=Pin.PULL_UP)
button2 = Pin(6, mode=Pin.IN, pull=Pin.PULL_UP)
button3 = Pin(5, mode=Pin.IN, pull=Pin.PULL_UP)
button4 = Pin(8, mode=Pin.IN, pull=Pin.PULL_UP)

button1_val = None
button2_val = None
button3_val = None
button4_val = None


M5.begin()

while True:
  M5.update()
  
  
  # read digital value from top button:
  button1_val = button1.value()
  button2_val = button2.value()
  button3_val = button3.value()
  button4_val = button4.value()
  
   
  # print ADC and button values to send them to the USB Serial port:
  print(button1_val, ',', button2_val, ',', button3_val, ',', button4_val)
  
  # some delay to make sure the data is not sent too fast:
  time.sleep_ms(50)




