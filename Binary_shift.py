from machine import Pin
from time import sleep

led_pins = [Pin(6, Pin.OUT), Pin(7, Pin.OUT), Pin(8, Pin.OUT), Pin(9, Pin.OUT)]

button_left = Pin(15, Pin.IN, Pin.PULL_DOWN)
button_right = Pin(16, Pin.IN, Pin.PULL_DOWN)

def display_binary(binary_value):
    for i in range(4):
        led_pins[i].value(int(binary_value[i]))

def left_shift(binary_value):
    return binary_value[1:] + "0"

def right_shift(binary_value):
    return "0" + binary_value[:-1]


binary_value = "0000"


while True:
    
    if binary_value == "0000":
        binary_value = input("""The current Binary value is 0,
enter a 4 bit binary value to continue: """)
        display_binary(binary_value)

    if button_left.value() == 1:
        binary_value = left_shift(binary_value)
        sleep(0.3)
        print(binary_value)

    if button_right.value() == 1:
        binary_value = right_shift(binary_value)
        sleep(0.3)
        print(binary_value)

    display_binary(binary_value)
    
    




