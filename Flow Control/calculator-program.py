# Calculator Program in Python

#Please select the operation:
#1. Add
#2. Subtract
#3. Multiply
#4. Divide

import sys

# Get the operation first
operation = int(input("Enter the operation: "))

# Check if operation is valid before proceeding
if operation not in [1, 2, 3, 4]:
    print("Invalid operation. Please select 1, 2, 3, or 4.")
    sys.exit(1)  # Exit with error code 1

# Only ask for numbers if operation is valid
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

# Perform the selected operation
if operation == 1:
    c = x + y
    print("The sum of the two numbers is", c)
elif operation == 2:
    c = x - y
    print("The difference of the two numbers is", c)
elif operation == 3:
    c = x * y
    print("The product of the two numbers is", c)
elif operation == 4:
    if y == 0:
        print("Error: Division by zero is not allowed")
        sys.exit(1)
    c = x / y
    print("The quotient of the two numbers is", c)

# ----------------------------------------------------------------





