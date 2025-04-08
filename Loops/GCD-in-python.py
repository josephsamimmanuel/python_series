# GCD in python
# STEPS:
# 1. Get the input from the user
# 2. Find minimum of the two numbers
# 3. Run a loop from minimum to 0 in descending order - range(min(a, b), 0, -1)
# 4. Check if the current number divides both the numbers without remainder - if a % i == 0 and b % i == 0
# 5. If yes, print the current number and break the loop - print(i) and break
# 6. If no, continue the loop - continue

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

# (a) Enter a number: 6
# (b) Enter another number: 9

# Logic for finding GCD

# Method 1: Using for loop

for i in range(min(a, b), 0, -1): # min(a, b) = 6 - range(6, 0, -1) = 6, 5, 4, 3, 2, 1
    if a % i == 0 and b % i == 0: # 6 % 6 = 0, 6 % 5 = 1, 6 % 4 = 2, 6 % 3 = 0, 6 % 2 = 0, 6 % 1 = 0 and 9 % 6 = 3, 9 % 5 = 4, 9 % 4 = 1, 9 % 3 = 0, 9 % 2 = 1, 9 % 1 = 0
        print(i)
        break
    
# ----------------------------------------------------------------
    
# Method 2: Using while loop

i = min(a, b)

while i > 0:
    if a % i == 0 and b % i == 0:
        print(i)
        break
    i -= 1

# ----------------------------------------------------------------
# Method 3: Using math.gcd

import math

print(math.gcd(a, b))

# ----------------------------------------------------------------

