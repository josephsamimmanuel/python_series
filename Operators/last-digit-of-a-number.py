# Last digit of a number

# Example:
# I/P : 12345
# O/P : 5

# I/P : 123456789
# O/P : 9

# I/P : 1234567890
# O/P : 0

# ----------------------------------------------------------------
# For positive numbers
n = int(input("Enter the number: "))
last_digit = n % 10
print(f"The last digit of {n} is {last_digit}")

# ----------------------------------------------------------------

# For negative numbers
n = int(input("Enter the number: "))
last_digit = abs(n) % 10
print(f"The last digit of {n} is {last_digit}")

# ----------------------------------------------------------------


