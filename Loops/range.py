# range is a function that returns a sequence of numbers.

# syntax:
# range(start, stop, step)

# example:

for i in range(1, 10, 2):
    print(i)

# ----------------------------------------------------------------

# example

r = range(10)
print(r)    # range(0, 10)

r = range(10, 20)
print(r)    # range(10, 20)

# ----------------------------------------------------------------

# example

l = list(r)
print(l)    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ----------------------------------------------------------------

# example

r = range(5)
print(type(r))    # <class 'range'>

# ----------------------------------------------------------------

# example : Range with two parameters

r = range(1, 10)
print(list(r))    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# ----------------------------------------------------------------

# example : Range with three parameters (start, stop, step)

r = range(1, 10, 2)
print(list(r))    # [1, 3, 5, 7, 9]

# ----------------------------------------------------------------

# example : Range with negative step        

r = range(10, 1, -1)
print(list(r))    # [10, 9, 8, 7, 6, 5, 4, 3, 2]

# ----------------------------------------------------------------

# example : Range

r = range(-2, 2, 1)
print(list(r))    # [-2, -1, 0, 1]

# ----------------------------------------------------------------


