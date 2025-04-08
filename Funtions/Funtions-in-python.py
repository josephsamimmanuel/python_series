# Functions in Python
# Function is a reusable block of code that performs a specific task.
# It can take input, process it, and return output.

# Define a function
def greet(name):
    print(f"Hello, {name}!")
    
# Call the function
greet("John")

# ----------------------------------------------------------------

def printDate(day, month, year):
    return f"{day}-{month}-{year}"

# Call the function
print("India got independence on:"+ printDate(15, 8, 1947))
print(printDate(15, 8, 1947))


# ----------------------------------------------------------------

def greet_msg():
    print("Hi")
    print("Hello")
    
def exit_msg():
    print("Please come again")
    print("Thank you")

greet_msg()
print("--------------------------------")
exit_msg()

# ----------------------------------------------------------------

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

print(add(10, 20))
print(sub(10, 20))
print(mul(10, 20))
print(div(10, 20))

# ----------------------------------------------------------------




