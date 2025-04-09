# returning multiple values in python

def add_sub(a, b):
    return a + b, a - b

print(add_sub(10, 20))

# unpacking the tuple
result = add_sub(10, 20)
print(result)

# unpacking the tuple
result1, result2 = add_sub(10, 20)
print(result1, result2)

# ------------------------------------------------------------

# returning multiple values from a function
def add_sub_mul_div(a, b):
    return a + b, a - b, a * b, a / b   # this is a tuple

result = add_sub_mul_div(10, 20)
print(result)

add, sub, mul, div = add_sub_mul_div(10, 20)
print(add, sub, mul, div)

# ------------------------------------------------------------

# returning multiple values from a function - in the form of a list
def add_sub_mul_div(a, b):
    return [a + b, a - b, a * b, a / b]  # this is a list

result = add_sub_mul_div(10, 20)
print(result)

# unpacking the list
add, sub, mul, div = add_sub_mul_div(10, 20)
print(add, sub, mul, div)

# ------------------------------------------------------------

# returning multiple values from a function - in the form of a dictionary
def add_sub_mul_div(a, b):
    return {"add": a + b, "sub": a - b, "mul": a * b, "div": a / b}

add_sub_mul_div(10, 20)

add, sub, mul, div = add_sub_mul_div(10, 20)
print(add, sub, mul, div)

# ------------------------------------------------------------









