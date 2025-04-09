# Default arguments

def fun(id, name="NA", age=None):
    # print(id, end=" ")
    # print(name, end=" ")
    # print(age, end=" ")
    print(id, name, age)

fun(10, "John", 20)
fun(10, "John")
fun(10)

# non default arguments must be before default arguments
def fun(id, name="", age=None):
    print(id, name, age)

fun(10, "John", 20)
fun(10, "John")
fun(10)
