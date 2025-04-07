# Tuple in python

# Tuple is a collection of items that are ordered and immutable.
# Tuple is defined using parentheses.
# Tuple can contain different types of data.
# Tuple is indexed from 0.

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)                              # (1, 2, 3, 4, 5)

# Accessing elements of a tuple
print(my_tuple[0])                           # 1

# Tuple is immutable
# my_tuple[0] = 10
print(my_tuple)                              # (1, 2, 3, 4, 5)

# Tuple can contain different types of data
my_tuple = (1, "Hello", 3.14, True)
print(my_tuple)                              # (1, "Hello", 3.14, True)

# Tuple can be nested
my_tuple = (1, (2, 3), 4)
print(my_tuple)                              # (1, (2, 3), 4)

# ----------------------------------------------------------------

# Tuple methods

# count()
my_next_tuple = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
print(my_next_tuple.count(1))                     # 2

# index()
my_next_tuple = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
print(my_next_tuple.index(1))                     # 0

# len()
my_next_tuple = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
print(len(my_next_tuple))                         # 10

# max()
my_next_tuple = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
print(max(my_next_tuple))                         # 5

# min()
my_next_tuple = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
print(min(my_next_tuple))                         # 1

# sum()
my_next_tuple = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
print(sum(my_next_tuple))                         # 30

# ----------------------------------------------------------------

# Tuple without parentheses
my_new_tuple = 1, 2, 3, 4, 5
print(my_new_tuple)                              # (1, 2, 3, 4, 5)
print(type(my_new_tuple))                        # <class 'tuple'>
print(my_new_tuple[0])                           # 1
print('Checking',my_new_tuple[1:3])                         # (2, 3)
print(1 in my_new_tuple)                         # True
print(my_new_tuple.count(1))                     # 1
print(my_new_tuple.index(1))                     # 0
print(len(my_new_tuple))                         # 5
print(max(my_new_tuple))                         # 5
print(min(my_new_tuple))                         # 1
print(sum(my_new_tuple))                         # 15

# Tuple with one element
single_element_tuple = (1,)
print(single_element_tuple)                              # (1,)

# Tuple unpacking - using the 5-element tuple we created earlier
a, b, c, d, e = my_new_tuple
print(a, b, c, d, e)                          # 1 2 3 4 5

# ----------------------------------------------------------------



