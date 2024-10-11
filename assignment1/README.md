## Assignment 01
Assignment 1 description:  
In this assignment, we are required to find an object in real life and transform it into a digital input, then connect it to an RGB light strip. This digital input can change the output, which is the state of the RGB light strip.  

Concept Sketches:  
[Repository README LINK](../README.md)  
[Assignment 1 Code Link](hw.py)  
```Python
while True:
    M5.update()  

    if input_pin.value() == True:  
        print('Pin 7 is HIGH, setting color to RED')
        rgb_strip.fill_color(0xff0000)  
    else:  
        print('Pin 7 is LOW, cycling through colors')
        color_cycle()

    time.sleep_ms(100)
```  
Image link example:
![diagram](diagram.png)  

List example  
* list 1
* list 2
* list 3
