def fun2():
    print("Inside fun2")

def fun1():
    print("Before fun2")
    fun2()
    print("After fun2")

# Main code
print("Before fun1")
fun1()
print("After fun1")

# OUTPUT:
# Before fun1 - 1
# Before fun2 - 2
# Inside fun2 - 3
# After fun2 - 4
# After fun1 - 5


