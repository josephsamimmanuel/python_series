# Id in python - gives the memory address of the variable

a = 10
b = 10

print(id(a))
print(id(b))

# ----------------------------------------------------------------

a = 10
b = 20

print(id(a))
print(id(b))

# ----------------------------------------------------------------

a = 10
b = 10
c = "Hello"
d = "Hello"

print(id(a))
print(id(b))
print(id(c))
print(id(d))

# ----------------------------------------------------------------

a = 10
b = 10

print(a is b)

c = a

print(c is b)

c = 20

print(c is b)

# ----------------------------------------------------------------




