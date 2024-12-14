import os, sys, io
import M5
from M5 import *
import time
import m5utils
from hardware import *
from machine import Pin, PWM

# 初始化 M5 板
M5.begin()

# 初始化按钮
button1 = Pin(1, mode=Pin.IN, pull=Pin.PULL_UP)
button2 = Pin(6, mode=Pin.IN, pull=Pin.PULL_UP)
button3 = Pin(5, mode=Pin.IN, pull=Pin.PULL_UP)
button4 = Pin(8, mode=Pin.IN, pull=Pin.PULL_UP)  # 用于控制舵机的按钮

# 初始化按钮状态变量
button1_val = None
button2_val = None
button3_val = None
button4_val = None

# 初始化舵机 (Pin 38)
pwm1 = PWM(Pin(38))
pwm1.freq(50)  # 设置 PWM 频率为 50Hz
duty_cycle = 0  # 初始占空比
pwm1.duty(duty_cycle)

# 定义舵机状态变量
current_state = 0  # 0 表示设置占空比为 65，1 表示设置占空比为 85
previous_button4_state = 1  # 按钮4的初始状态（未按下）

# 主循环
while True:
    M5.update()

    # 读取所有按钮状态
    button1_val = button1.value()
    button2_val = button2.value()
    button3_val = button3.value()
    button4_val = button4.value()

    # 打印按钮状态
    print(button1_val, ',', button2_val, ',', button3_val, ',', button4_val)

    # 按钮 4 的逻辑（控制舵机）
    if previous_button4_state == 1 and button4_val == 0:  # 检测按钮从未按下到按下
        if current_state == 0:
            #print("Button 4 pressed: Setting duty cycle to 65.")
            pwm1.duty(69)  # 设置占空比为 69（舵机旋转）
            time.sleep(2)  # 持续 2 秒
            #print("Stopping servo.")
            pwm1.duty(0)  # 停止舵机
            current_state = 1  # 切换到下一个状态
        elif current_state == 1:
            #print("Button 4 pressed: Setting duty cycle to 85.")
            pwm1.duty(85)  # 设置占空比为 85（舵机旋转）
            time.sleep(2)  # 持续 2 秒
            #print("Stopping servo.")
            pwm1.duty(0)  # 停止舵机
            current_state = 0  # 切换到下一个状态

    # 更新按钮 4 的上一次状态
    previous_button4_state = button4_val

    # 添加延迟，避免数据发送过快
    time.sleep(0.1)

