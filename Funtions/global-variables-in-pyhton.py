# global variables in python

def fun():
    a = 20  # this is a local variable
    b = 30  # this is a local variable
    print(a,b,c,d)
    
c=30 # this is a global variable
d=40 # this is a global variable
print(c,d)

# ------------------------------------------------------------

def fun():
    x=10 # this is a local variable
x=15 # this is a global variable
fun()
print(x) 

# The output will be 15 because the local variable x is used inside the function and the global variable x is not used.
# The global variable x is not affected by the local variable x.
# The local variable x is not affected by the global variable x.
# So the output is 15.

def fun():
    global x
    x=10 # this is a local variable
x=15 # this is a global variable
fun()
print(x) 

# The output will be 10 because the global variable x is used inside the function and the local variable x is not used.
# The global variable x is affected by the local variable x.
# The local variable x is not affected by the global variable x.
# So the output is 10.

# ------------------------------------------------------------

def fun():
    y = x + 10 # this is a local variable - x is a global variable
    print(y)

x = 10
fun()

# The output will be 20 because the global variable x is used inside the function and the local variable x is not used.
# The global variable x is affected by the local variable x.
# The local variable x is not affected by the global variable x.
# So the output is 20.

# ------------------------------------------------------------

def fun():
    x = x + 10 # this is a local variable - x is a global variable
    print(x)

x = 10
fun()

# The output will be an error because the local variable x is used inside the function and the global variable x is not used.
# The global variable x is not affected by the local variable x.
# The local variable x is not affected by the global variable x.
# So the output is an error.

# ------------------------------------------------------------

def fun():
    x = 10 # this is a local variable
    globals()['x'] = 20 # this is a global variable
    print(x)

x = 10
fun()
print(x)

# output
# 10
# 20

# The output will be 20 because the global variable x is used inside the function and the local variable x is not used.
# The global variable x is affected by the local variable x.
# The local variable x is not affected by the global variable x.
# So the output is 20.





