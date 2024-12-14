import js as p5
from js import document
import random

# 加载资源
sound_shoot = p5.loadSound('shoot.wav')
sound_mario = p5.loadSound('mario.mp3')
sound_mushroom = p5.loadSound('mushroom.mp3')
sound_star = p5.loadSound('star.mp3')
sound_title = p5.loadSound('title.mp3')

title_img = p5.loadImage('title.webp')
coin_img = p5.loadImage('coin.png')
mushroom_img = p5.loadImage('mushroom.png')
star_img = p5.loadImage('star.png')

sound_played_title = False
sound_played_button1 = False  # 防止按钮1音频重复播放
sound_played_button2 = False  # 防止按钮2音频重复播放

random_number = None  # 按钮1的随机数
random_image = None  # 按钮2随机选择的图像
data = None  # 存储按钮状态数据

button1_state = 1
button2_state = 1
program_state = 'TITLE'

def setup():
    p5.createCanvas(500, 300)
    p5.textSize(32)
    p5.textAlign(p5.CENTER, p5.CENTER)
    p5.imageMode(p5.CENTER)

def draw():
    global button1_state
    global button2_state
    global program_state
    global sound_played_title, sound_played_button1, sound_played_button2
    global random_number, random_image, data

    # 获取 HTML 中的数据
    data = document.getElementById("data").innerText
    data_list = data.split(',')

    # 假设按钮1的状态在第一个值，按钮2的状态在第二个值
    button1_val = int(data_list[0]) if len(data_list) > 0 else 0
    button2_val = int(data_list[1]) if len(data_list) > 1 else 0

    button2_state = button2_val
    button1_state = button1_val

    if program_state == 'TITLE':
        if not sound_played_title:
            sound_title.play()  # 播放标题音乐
            sound_played_title = True
        p5.background(255)
        p5.image(title_img, p5.width / 2, p5.height / 3, 100)  # 显示标题图片
        p5.fill(0)
        p5.text('Start', p5.width / 2, 2 * p5.height / 3)  # 显示文字 Start

    # button1 pressed (button_val changed to 0)
    if button1_state == 1 and button2_state == 0:
      program_state = 'QUESTION'
      # update button1 last value:
      button2_state = 0

    if button2_state == 1 and button1_state == 0:
      program_state = 'DICE'
      # update button1 last value:
      button1_state = 0

    print(program_state)
    print(button1_state)
    print(button2_state)

    # 按钮1的逻辑：生成随机数字并播放 shoot.wav
    if button1_val == 1:
        if not sound_played_button1:
            random_number = random.randint(1, 3)  # 生成1到3的随机数
            sound_shoot.play()  # 播放音频
            sound_played_button1 = True  # 标记音频已播放
    else:
        sound_played_button1 = False  # 重置音频播放状态

    # 按钮2的逻辑：随机选择图像并播放对应音频
    if button2_val == 1:
        if not sound_played_button2:
            random_choice = random.choice(['coin', 'mushroom', 'star'])
            if random_choice == 'coin':
                random_image = coin_img
                sound_mario.play()
            elif random_choice == 'mushroom':
                random_image = mushroom_img
                sound_mushroom.play()
            elif random_choice == 'star':
                random_image = star_img
                sound_star.play()
            sound_played_button2 = True
    else:
        sound_played_button2 = False  # 重置音频播放状态

    # 绘制画布
    p5.background(255)  # 白色背景
    
    if program_state == 'DICE':
      # 显示随机数字
      if random_number is not None:
          p5.fill(0)
          p5.text(f"{random_number} Step", p5.width / 2, p5.height / 2)

    if program_state == 'QUESTION':
      # 显示随机选择的图像
      if random_image is not None:
          p5.image(random_image, p5.width / 2, p5.height / 2, 100, 100)