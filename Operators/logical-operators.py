# Logical Operators in Python

# and
# or
# not

# and
a = True
b = False
print(a and b)          # False

# or
a = True
b = False
print(a or b)          # True

# not
a = True
print(not a)          # False

# ------------------------------------------------------------

a=10
b=20
c=30

print(a<b and b<c)          # True
print(a<b and b>c)          # False
print(not a>b)          # True

# ------------------------------------------------------------

s1=""
s2=s1 or "Hello"
print(s2)          # Hello

s1="Hello"
s2=s1 or "World"
print(s2)          # Hello

# Applicable for strings, lists, tuples, dictionaries, sets, etc.

# ------------------------------------------------------------

# x or y - if x is true, then x, otherwise y
x = 10
print(x or 20)          # 10

y=0 # False - 0, "", None, False, etc.
print(y or 20)          # 20

# ------------------------------------------------------------
