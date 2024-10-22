from machine import Pin

led_pins = [Pin(2, Pin.OUT), Pin(3, Pin.OUT), Pin(4, Pin.OUT), Pin(5, Pin.OUT),Pin(6, Pin.OUT)]


# Function for binary addition
def binary_addition(number_1, number_2):
    total = ""
    carry = 0

    for i in range(3, -1, -1):
        bit_total = int(number_1[i]) + int(number_2[i]) + carry
        if bit_total == 0 or bit_total == 1:
            total = str(bit_total) + total
            carry = 0
            led_pins[i].value(bit_total)
        elif bit_total == 2:
            total = "0" + total
            carry = 1
            led_pins[i].value(0)
            
        elif bit_total == 3:
            total = "1" + total
            carry = 1
            led_pins[i].value(1)
            
    led_pins[4].value(carry)
    print (carry,total)

while True:

    number_1 = input("Enter a 4-bit binary number: ")
    number_2 = input("Enter a 2nd 4-bit binary number: ")
    binary_addition(number_1, number_2)
    






