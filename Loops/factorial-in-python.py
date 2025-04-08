# Factorial in python

# n! = n * (n-1) * (n-2) * ... * 1
# n! = n * (n-1)!

# I/P: 5
# O/P: 120

# ----------------------------------------------------------------

n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n+1):
    factorial *= i

print(factorial)

# I/P: 5
# O/P: 120

# ----------------------------------------------------------------

# Factorial using while loop

n = int(input("Enter a number: "))

factorial = 1

i = 1

while i <= n:
    factorial *= i
    i += 1

print(factorial)

# I/P: 5
# O/P: 120

# ----------------------------------------------------------------

# Factorial of 10

factorial = 1

for i in range(1, 11): # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    factorial *= i # factorial = factorial * i  # 1 * 1 = 1, 1 * 2 = 2, 2 * 3 = 6, 6 * 4 = 24, 24 * 5 = 120, 120 * 6 = 720, 720 * 7 = 5040, 5040 * 8 = 40320, 40320 * 9 = 362880, 362880 * 10 = 3628800

print(factorial)

# ----------------------------------------------------------------

import math

n = int(input("Enter a number Using math.factorial: "))

print(math.factorial(n))

# I/P: 5
# O/P: 120


