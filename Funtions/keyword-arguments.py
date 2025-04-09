# Keyword arguments

def fun(id, name, age):
    print(id, name, age)

fun(10, "John", 20)                 # positional arguments
fun(id=10, name="John", age=20)     # keyword arguments
fun(id=10, name="John")             # keyword arguments
fun(id=10)                          # keyword arguments

# keyword arguments must be after positional arguments
def fun(id, name, age):
    print(id, name, age)

fun(10, "John", age=20)

# keyword argument can be used to change the order of arguments
def fun(id, name, age):
    print(id, name, age)

fun(age=20, id=10, name="John")


