# if, else, elif are used to check the condition and execute the code accordingly.

# if condition:
#     code
# 4 spaces # Statements to be executed if the condition is true
        
# elif condition:
#     code
# 4 spaces # Statements to be executed if the first condition is false and the second condition is true
        
# else:
#     code
# 4 spaces # Statements to be executed if all the conditions are false
        
# ----------------------------------------------------------------

# Example:
# Find EVEN or ODD

n = int(input("Enter a number: "))

if n % 2 == 0:
    print("EVEN")
else:
    print("ODD")

# ----------------------------------------------------------------

# Find POSITIVE or NEGATIVE or ZERO

n = int(input("Enter a number: "))

if n > 0:
    print("POSITIVE")
elif n < 0:
    print("NEGATIVE")
else:
    print("ZERO")

# ----------------------------------------------------------------

# Find the largest of the three numbers

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a > b and a > c:
    print("A is the largest number")
elif b > a and b > c:
    print("B is the largest number")
else:
    print("C is the largest number")

# ----------------------------------------------------------------

# Decide if an input number is:
# 1. Positive Even
# 2. Positive Odd
# 3. Negative Even
# 4. Negative Odd
# 5. Zero

n = int(input("Enter a number: "))

if n > 0:
    if n % 2 == 0:
        print("Positive Even")
    else:
        print("Positive Odd")
elif n < 0:
    if n % 2 == 0:
        print("Negative Even")
    else:
        print("Negative Odd")
else:
    print("Zero")
    
# ----------------------------------------------------------------

# Decide if an input is a vowel or consonant

n = input("Enter a character: ")

if n in ['a', 'e', 'i', 'o', 'u']:
    print("Vowel")
else:
    print("Consonant")
    
# ----------------------------------------------------------------

# Decide if an input is a digit or not

n = input("Enter a character: ")

if n.isdigit():
    print("Digit")
else:
    print("Not a digit")
    
# ----------------------------------------------------------------

# Take two numbers a and b from the user and depending upon the values of a and b, print the result of the following:
# 1. a is greater
# 2. b is greater
# 3. a is equal to b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    print("a is greater")
elif b > a:
    print("b is greater")
else:
    print("a is equal to b")
    
# ----------------------------------------------------------------