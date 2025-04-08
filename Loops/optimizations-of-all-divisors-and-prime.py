# OPTIMIZATIONS OF ALL DIVISORS AND PRIME NUMBER
# STEPS:
# 1. Get the input from the user
# 2. Run a loop from 1 to int(math.sqrt(n)) + 1
# 3. Check if the current number divides n without remainder - if n % i == 0
# 4. If yes, print the current number - print(i)
# 5. To avoid printing the square root twice, check if i != n // i
# 6. Print the pair divisor - print(n // i)
# 7. Run a loop from 3 to int(math.sqrt(n)) + 1, with a step of 2
# 8. Check if the current number divides n without remainder - if n % i == 0
# 9. If yes, return False
# 10. If no, continue the loop
# 11. If the loop completes without returning False, return True

import math

n = int(input("Enter a number: "))

print("\n=== Finding All Divisors ===")

# Method 1: Optimized for loop - O(sqrt(n))
print("\nMethod 1 (Optimized for loop):")
for i in range(1, int(math.sqrt(n)) + 1):
    if n % i == 0:
        print(i)  # Print the divisor
        if i != n // i:  # To avoid printing the square root twice
            print(n // i)  # Print the pair divisor

# ----------------------------------------------------------------

# Method 2: Optimized while loop - O(sqrt(n))
print("\nMethod 2 (Optimized while loop):")
i = 1
while i <= math.sqrt(n):
    if n % i == 0:
        print(i)  # Print the divisor
        if i != n // i:  # To avoid printing the square root twice
            print(n // i)  # Print the pair divisor
    i += 1

# ----------------------------------------------------------------

# Method 3: Optimized recursion - O(sqrt(n))
def divisors(n, i=1):
    if i > math.sqrt(n):
        return
    if n % i == 0:
        print(i)  # Print the divisor
        if i != n // i:  # To avoid printing the square root twice
            print(n // i)  # Print the pair divisor
    divisors(n, i + 1)

print("\nMethod 3 (Optimized recursion):")
divisors(n)

# ----------------------------------------------------------------

# Prime number check - O(sqrt(n))
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:  # Quick check for even numbers
        return False
    
    # Check only odd numbers up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

print("\n=== Prime Number Check ===")
if is_prime(n):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")  

