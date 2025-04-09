# find the first digit of a number

def find_first_digit(number):               # 232
    while number >= 10:                     # 232 >= 10
        number = number // 10               # 232 // 10 = 23
    return number                           # return 23

print(find_first_digit(int(input("Enter a number: "))))

# ------------------------------------------------------------

import math

def find_first_digit(number):
    return int(math.log10(number))

print(find_first_digit(int(input("Enter a number: "))))

