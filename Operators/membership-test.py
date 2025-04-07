# Membership Test in Python

# in
# not in

# in - checks if a value exists in a sequence
a = "Hello, World!"
print("Hello" in a)          # True

# not in - checks if a value does not exist in a sequence
print("Hello" not in a)          # False

s="geeks for geeks"

print("for" in s)          # True
print("gk" in s)          # False

# ------------------------------------------------------------

d = {10: "abc", 20: "def"}

print(10 in d)          # True
print(20 in d)          # True
print(30 in d)          # False
print("abc" in d)          # False

# ------------------------------------------------------------

l = [1,2,3,4,5]

print(1 in l)          # True
print(6 in l)          # False
print([1,2,3] in l)          # False

# ------------------------------------------------------------

# in - checks if a value exists in a sequence

t = (1,2,3,4,5)

print(1 in t)          # True
print(6 in t)          # False

# ------------------------------------------------------------







