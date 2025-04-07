# Identity Operators in Python

# is
# is not

# is - checks if two variables point to the same object
a = 10
b = 10
print(a is b)          # True

# is not - checks if two variables do not point to the same object
a = 10
b = 20
print(a is not b)          # True

# ------------------------------------------------------------

x1 = 10
x2 = 10
y1 = 10
y2 = 20
z1 ="joseph"
z2 ="joseph"

print(x1 is x2)          # True
print(y1 is y2)          # False
print(z1 is z2)          # True

# ------------------------------------------------------------

a = 10 
a = b

print(a is b)          # True

# ------------------------------------------------------------

l1 = [1,2,3]
l2 = [1,2,3]

print(l1 is l2)          # False

# True only if they are literals
# not applicable for lists, dictionaries, tuples, etc.






