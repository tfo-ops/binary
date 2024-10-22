from machine import Pin
from time import sleep

# Set up the LEDs
led_1 = Pin(2, Pin.OUT)
led_2 = Pin(3, Pin.OUT)
led_4 = Pin(4, Pin.OUT)
led_8 = Pin(5, Pin.OUT)

# Set up the buttons
button_inc = Pin(14, Pin.IN, Pin.PULL_DOWN)
button_dec = Pin(15, Pin.IN, Pin.PULL_DOWN)

# Initialize the counter
counter = 0

def update_leds(value):
    """
    Updates the LEDs to represent the binary value of the counter using bitwise manipulation.
    """
    led_1.value((value >> 0) & 1)
    led_2.value((value >> 1) & 1)
    led_4.value((value >> 2) & 1)
    led_8.value((value >> 3) & 1)

while True:
    # Check if the increment button is pressed
    if button_inc.value():
        counter += 1
        if counter > 15:  # Ensure counter stays within 4-bit range
            counter = 15
        print(f"Counter value: {counter}")
        update_leds(counter)
        sleep(0.2)  # Debounce delay

    # Check if the decrement button is pressed
    if button_dec.value():
        counter -= 1
        if counter < 0:  # Ensure counter doesn't go negative
            counter = 0
        print(f"Counter value: {counter}")
        update_leds(counter)
        sleep(0.2)  # Debounce delay
