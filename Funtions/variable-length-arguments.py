def fun(*args): # *args is a variable length argument - is tuple
    result = 0
    for i in args:
        result += i
    return result

print(fun(1, 2, 3, 4, 5))
print(fun(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(fun(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))

#OUTPUT
# 15
# 55
# 120

# ------------------------------------------------------------------------------------------------

def fun(initial, *args): # initial is a keyword argument
    result = initial
    for i in args:
        result += i
    return result

print(fun(1, 2, 3, 4, 5))


# ------------------------------------------------------------------------------------------------
# *args is a variable length argument - is tuple | Positional arguments
def fun(*args):
    print(args)

fun(1, 2, 3, 4, 5)

#OUTPUT
# (1, 2, 3, 4, 5)

# ------------------------------------------------------------------------------------------------
# **args is a variable length argument - is dictionary | Keyword arguments
def fun(**args):
    print(args)

fun(a=1, b=2, c=3, d=4, e=5)

#OUTPUT
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# ------------------------------------------------------------------------------------------------

# *args and **kwargs can be used together
def fun(*args, **kwargs):
    print(args)
    print(kwargs)

fun(1, 2, 3, 4, 5, a=1, b=2, c=3, d=4, e=5)

#OUTPUT
# (1, 2, 3, 4, 5)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}      

# ------------------------------------------------------------------------------------------------
# *args and **kwargs can be used together
def fun(id,**kwargs):
    print(f"The id is: {id} , The kwargs are: {kwargs}", end=" ") # The id is: 101 , The kwargs are: {'name': 'John', 'age': 20, 'city': 'New York'} Details of id: 101
    # id is a positional argument
    # **kwargs is a keyword argument
    # id must be before **kwargs
    # keyword arguments must be after positional arguments
    # keyword arguments can be used to change the order of arguments
    print(f"Details of id: {id}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

fun(101, name="John", age=20, city="New York")
print("--------------------------------")
fun(102, name="Jane", age=21, city="Los Angeles")


# OUTPUT
# The id is: 101 , The kwargs are: {'name': 'John', 'age': 20, 'city': 'New York'} Details of id: 101
# name: John
# age: 20
# city: New York

# --------------------------------------------------------------------------------------------------


