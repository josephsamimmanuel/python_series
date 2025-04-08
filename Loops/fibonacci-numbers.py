# Fibonacci numbers

n = int(input("Enter a number: "))

# Method 1: Using for loop

a = 0
b = 1

for i in range(n):
    print(a)
    temp = a
    a = b
    b = temp + b
    

# ----------------------------------------------------------------

# Method 2: Using while loop        

a = 0
b = 1

while a < n:
    print(a)
    a, b = b, a + b

# ----------------------------------------------------------------

# Method 3: Using recursion

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(n))

