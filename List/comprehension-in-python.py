# Comprehension in Python

# List Comprehension
#======================

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l1 = [i for i in l]

print(l1)                               # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# get list the numbers smaller than 5
l2 = [i for i in l if i < 5]
print(l2)                               # [1, 2, 3, 4]

# get list the numbers smaller than 5 and greater than 2
l3 = [i for i in l if i < 5 and i > 2]
print(l3)                               # [3, 4]

# get list the numbers even and odd
l4 = [i for i in l if i % 2 == 0]
print(l4)                               # [2, 4, 6, 8, 10]

l5 = [i for i in l if i % 2 != 0]
print(l5)                               # [1, 3, 5, 7, 9]

s = 'Hello World'

s1 = [i for i in s if i != ' ' and i != 'e']
print(s1)                               # ['H', 'l', 'l', 'o', 'W', 'r', 'l', 'd']

l2 = ["geeks", "ide", "courses", "gfg"]
l3 = [i for i in l2 if i.startswith('g')]
print(l3)                               # ['geeks', 'gfg']

l4 = [ i for i in range(10)]
print(l4)                               # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l5 = [ i for i in range(10) if i % 2 == 0]
print(l5)                               # [0, 2, 4, 6, 8]

l6 = [ i for i in range(10) if i % 2 != 0]
print(l6)                               # [1, 3, 5, 7, 9]

l7 = ["geeks", "for", "geeks", "gfg", "ide"]
l8 = [i.upper() for i in l7 if i.startswith('g')]
print(l8)                               # ['GEEKS', 'GEEKS', 'GFG']

l9 = [i.upper() for i in l7 if i.startswith('g') and len(i) > 3]
print(l9)                               # ['GEEKS', 'GEEKS']

# ------------------------------------------------------------

# Dictionary Comprehension
#=========================

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

d1 = {k: v for k, v in d.items()}

print(d1) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# ------------------------------------------------------------

# Set Comprehension
#==================
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

s1 = {i for i in s}
s2 = {i for i in s if i % 2 == 0}
s3 = {i for i in s if i % 2 != 0}

print(s1) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(s2) # {2, 4, 6, 8, 10}
print(s3) # {1, 3, 5, 7, 9}

# ------------------------------------------------------------




