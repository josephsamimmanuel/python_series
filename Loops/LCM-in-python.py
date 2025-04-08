# LCM in python

# STEPS:
# 1. Get the input from the user
# 2. Find maximum of the two numbers
# 3. Run a loop from maximum to a*b in ascending order - range(max(a, b), a*b+1)
# 4. Check if the current number divides both the numbers without remainder - if i % a == 0 and i % b == 0
# 5. If yes, print the current number and break the loop - print(i) and break
# 6. If no, continue the loop - continue

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

# (a) Enter a number: 12
# (b) Enter another number: 6


# Method 1: Using for loop

for i in range(max(a, b), a*b+1): # max(a, b) = 12 - range(12, 72+1) = 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72
    if i % a == 0 and i % b == 0: # 12 % 12 = 0, 12 % 6 = 0 and 13 % 12 = 1, 13 % 6 = 1 and so on
        print(i)
        break
    
# ----------------------------------------------------------------

# Method 2: Using while loop

i = max(a, b)

while i <= a*b:
    if i % a == 0 and i % b == 0:
        print(i)
        break
    i += 1
    
# ----------------------------------------------------------------

# Method 3: Using math.lcm

import math

print(math.lcm(a, b))

# ----------------------------------------------------------------



