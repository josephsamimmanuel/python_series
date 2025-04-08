# ALL DIVISORS OF A NUMBER
# STEPS:
# 1. Get the input from the user
# 2. Run a loop from 1 to n + 1 - range(1, n + 1)
# 3. Check if the current number divides n without remainder - if n % i == 0
# 4. If yes, print the current number - print(i)

n = int(input("Enter a number: "))

# Method 1: Using for loop

for i in range(1, n + 1):
    if n % i == 0:
        print(i)

# ----------------------------------------------------------------  

# Method 2: Using while loop

i = 1

while i <= n:
    if n % i == 0:
        print(i)
    i += 1

# ----------------------------------------------------------------

# Method 3: Using recursion

def divisors(n, i=1):
    if i > n:
        return
    if n % i == 0:
        print(i)
    divisors(n, i + 1)
    


