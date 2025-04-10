# formatted strings

# formatted strings are strings that are formatted using the format() method
# they are denoted by the f prefix
# Example:
# string = f"hello {name}"

# ------------------------------------------------------------------------------------------------

# Using % (like C language)

# %s - string
# %d - integer
# %f - float
# %x - hexadecimal
# %o - octal

# Example:
name = "John"
course = "Python"
s = "Welcome %s to the %s course" % (name, course)
print(s)

# ------------------------------------------------------------------------------------------------

# Using format() method

# Example:
name = "John"
course = "Python"
s = "Welcome {} to the {} course".format(name, course)
print(s)

# ------------------------------------------------------------------------------------------------

# Using f-string (like C language)

# Example:
name = "John"
course = "Python"
s = f"Welcome {name} to the {course} course"
print(s)

# ------------------------------------------------------------------------------------------------

s1 = "Hello"
s2 = "John"

print(f"{s1} {s2.upper()}") # we can use methods on the f-string
print(f"{s1.lower()} {s2}")
