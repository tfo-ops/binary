from machine import Pin
from time import sleep
button_add = Pin(14, Pin.IN, Pin.PULL_DOWN)
button_minus = Pin(15, Pin.IN, Pin.PULL_DOWN)


led_1 = Pin(2, Pin.OUT)
led_2 = Pin(3, Pin.OUT)
led_4 = Pin(4, Pin.OUT)
led_8 = Pin(5, Pin.OUT)
counter = 0
           
while True:
    if button_add.value()==1:
        sleep(0.3)
        counter +=1
        print(counter)
    if button_minus.value()==1:
        sleep(0.3)
        counter -=1
        print(counter)
    if counter == 1:
        led_1.value(1)
        led_2.value(0)     
        led_4.value(0)
        led_8.value(0)
    elif counter == 2:
        led_1.value(0)
        led_2.value(1)     
        led_4.value(0)
        led_8.value(0)
    elif counter == 3:
        led_1.value(1)
        led_2.value(1)     
        led_4.value(0)
        led_8.value(0)
    elif counter == 4:
        led_1.value(0)
        led_2.value(0)     
        led_4.value(1)
        led_8.value(0)
    elif counter == 5:
        led_1.value(1)
        led_2.value(0)     
        led_4.value(1)
        led_8.value(0)
    elif counter == 6:
        led_1.value(0)
        led_2.value(1)     
        led_4.value(1)
        led_8.value(0)
    elif counter == 7:
        led_1.value(1)
        led_2.value(1)     
        led_4.value(1)
        led_8.value(0)
    else:
        counter = 0
        led_1.value(0)
        led_2.value(0)     
        led_4.value(0)
        led_8.value(0)
        

