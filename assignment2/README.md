## Assignment 02
### Assignment 2 description:  
In this assignment, we were required to use an ADC sensor as an input and have several different output methods. I chose an RGB LED strip as the physical output. After connecting it to the web file, digital outputs are represented on the screen as visuals and sound.

To achieve this, I designed a toy inspired by the flag in the Super Mario game. When the user pulls Mario down, the flag on the other side rises. At the same time, the distance sensor beneath Mario triggers changes in the RGB LED strip's colors and updates the content on the webpage based on the distance.

### Concept Sketches:  
![concept_sketches](sketch.png)  

### State Diagram:  
When running the program initialize the RGB pin and input pin. When the value from digital input is high/1, print: Pin 7 is HIGH, setting color to RED and set RGB strip to red color. Else print: Pin 7 is LOW, cycling through colors and setting RGB strip color to start looping different colors.  

![state_diagram](diagram.png)  

### Hardware:  
* ATOM s3
* wires
* RGB Strip
* MDF boards
* distance senser

### Firmware:
[Assignment 2 Code for ATOM S3 Link](code.py)  

First, we need to set two different functions for two statuses, The first one is to keep a red light when the weapon is not on the base support, and the other one is RGB looping when the gun is on the base. Then we need to write a looping function to switch these two status by getting the value from pin 7.  

```Python
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
```

[Assignment 2 Code for Web Link](main.py)  

```Python
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
```

### Physical Components:
To make the toy gun work as a digital input, I need to add something to connect it to the breadboard. So I use copper foil tape to tape the button of the gun and the part of the base that holds the gun. So when I place the gun on the base, it will work like a button.  

![physical_components](components.jpg)

### Project outcome:
Finally, I made it work. When the gun is not on the base the RGB strip will keep glowing red light, and when I place the gun on the base, the RGB strip will start looping different color lights.
[Video for the outcome](outcome.mp4)  
![outcome](final_1.jpg)
![outcome](web_1.png)
![outcome](final_2.jpg)
![outcome](web_2.png)
