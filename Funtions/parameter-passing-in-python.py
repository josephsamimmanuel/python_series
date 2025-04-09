# Parameter passing in python - X

# Passing an integer
def fun(a):
    a = 10
    print(a)

fun(1)

# OUTPUT
# 10

# ------------------------------------------------------------------------------------------------

# Passing a list
def fun(a):
    a[0] = 10
    print(a)

fun([1, 2, 3, 4, 5])

# OUTPUT
# [10, 2, 3, 4, 5]

# ------------------------------------------------------------------------------------------------

def fun(a):
    a = 15  # a is a local variable
a=10        # a is a global variable
fun(a)      # a=10 is passed as a parameter
print(a)    # a=10 is printed

# OUTPUT
# 10

# ------------------------------------------------------------------------------------------------

def fun(a):
    a.append(10) # a is a local variable

a=[1,2,3,4,5]   # a is a global variable
fun(a)          # a=[1,2,3,4,5] is passed as a parameter
print(a)        # a=[1,2,3,4,5,10] is printed

# OUTPUT
# [1, 2, 3, 4, 5, 10]



