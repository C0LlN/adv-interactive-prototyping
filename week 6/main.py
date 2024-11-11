import js as p5
from js import document

mario_img = p5.loadImage('mario.png')
flag_img = p5.loadImage('flag.png')
sound = p5.loadSound('Mario.mp3')
sound_played = False

data = None

def setup():
    p5.createCanvas(500, 500)
    print('hello p5!')

def draw():
    global sound_played
    p5.background(255)

    global data
    
    data = document.getElementById("data").innerText

    
    data_value = int(data)

    y_position = p5.map(data_value, 0, 200, 420, 0)  

    opposite_y_position = p5.map(data_value, 0, 200, 0, 500)

    

    p5.image(flag_img, 260, opposite_y_position, 77, 50)  

    p5.rect(250, 0, 10, 500)

    p5.image(mario_img, 198, y_position, 80, 80)  

    

    if p5.millis() > 3000:
        if data_value < 90:
            #if not sound.isPlaying():
            if not sound_played:
                sound.play()
                sound_played = True
        else:
            sound_played = False

def print_test(x):
    print(x)
