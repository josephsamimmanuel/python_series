# 13.3 List Slicing in Python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numbers[::2]) # [::2] is the list of even numbers

print(numbers[1::2]) # [1::2] is the list of odd numbers

print(numbers[::-1]) # [::-1] is the reverse of the list

print(numbers[2:5]) # [2:5] is the list of numbers from index 2 to 4

print(numbers[2:5:2]) # [2:5:2] is the list of numbers from index 2 to 4 with a step of 2

# ------------------------------------------------------------

# Slicing (list, tuple, string)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]               # list

# list slicing
print(numbers[2:5]) # [2:5] is the list of numbers from index 2 to 4

# tuple slicing
numbers_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)         # tuple
print(numbers_tuple[2:5]) # (2, 3, 4)

# string slicing
text = "Hello, World!"                                  # string
print(text[2:5]) # "ll"

# ------------------------------------------------------------

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(l[-1 : -6: -1]) # [10, 9, 8, 7, 6]

print(l[::1]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(l[::-2]) # [10, 8, 6, 4, 2]

# ------------------------------------------------------------

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l2 = l1[:]

t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

t2 = t1[:]

s1 = "Hello, World!"

s2 = s1[:]

print(l1 is l2) # False - because l1 and l2 are different objects

print(t1 is t2) # True - because t1 and t2 are the same object | because tuple is immutable

print(s1 is s2) # True - because s1 and s2 are the same object | because string is immutable

# ------------------------------------------------------------




