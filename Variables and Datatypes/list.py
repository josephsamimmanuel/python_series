# List in python

# List is a collection of items that are ordered and mutable.
# List is defined using square brackets.
# List can contain different types of data.
# List is indexed from 0.

# Creating a list
my_list = [1, 2, 3, 4, 5]
print(my_list)                              # [1, 2, 3, 4, 5]
print(my_list[3])                           # 4
print(my_list[-1])                          # 5
print(my_list[-2])                          # 4
print(my_list[1:3])                         # [2, 3]
print(my_list[1:])                          # [2, 3, 4, 5]
print(my_list[:3])                          # [1, 2, 3]
print(my_list[:])                           # [1, 2, 3, 4, 5]

# Accessing elements of a list
print(my_list[0])                           # 1

# Adding elements to a list
my_list.append(6)
print(my_list)                              # [1, 2, 3, 4, 5, 6]

# Removing elements from a list
my_list.remove(3)
print(my_list)                              # [1, 2, 4, 5, 6]

# insert elements to a list
my_list.insert(1, 3)
print(my_list)                              # [1, 3, 2, 4, 5, 6]

# extend elements to a list
my_list.extend([7, 8, 9])
print(my_list)                              # [1, 3, 2, 4, 5, 6, 7, 8, 9]

# check if an element is in a list
print(9 in my_list)                         # True
print(10 in my_list)                        # False

# count elements in a list
print(my_list.count(3))                     # 1

# find the index of an element in a list
print(my_list.index(3))                     # 1

# find the length of a list
print(len(my_list))                         # 9

# find the maximum element in a list
print(max(my_list))                         # 9

# find the minimum element in a list
print(min(my_list))                         # 1

# find the sum of elements in a list
print(sum(my_list))                         # 45

# sort elements in a list
my_list.sort()
print(my_list)                              # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# reverse elements in a list
my_list.reverse()
print(my_list)                              # [9, 8, 7, 6, 5, 4, 3, 2, 1]

# find the average of elements in a list
print(sum(my_list) / len(my_list))          # 5.0

# find the median of elements in a list
print(sorted(my_list)[len(my_list) // 2])    # 5

# find the mode of elements in a list
print(max(set(my_list), key=my_list.count))  # 3

# find the range of elements in a list
print(max(my_list) - min(my_list))          # 8

# find the variance of elements in a list
print(sum((x - sum(my_list) / len(my_list)) ** 2 for x in my_list) / len(my_list))  # 6.0

# find the mean of elements in a list
print(sum(my_list) / len(my_list))          # 5.0

# clear elements in a list
my_list.clear()
print(my_list)                              # []

# ----------------------------------------------------------------

my_new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_new_list)                              # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# delete the elements at index 0 and 1 from a list
del my_new_list[0:3]
print(my_new_list)                              # [4, 5, 6, 7, 8, 9]

# delete the list
del my_new_list

# ----------------------------------------------------------------

my_array = [1, 2, 3, 4, 5]

# remove elements from a list
my_array.remove(3)
print(my_array)                              # [1, 2, 4, 5]

# remove the last element from a list
my_array.pop()
print(my_array)                              # [1, 2, 4]

# remove the element at index 1 from a list
my_array.pop(1)
print(my_array)                              # [1, 4]

# insert the element 2 at index 1 in a list
my_array.insert(1, 2)
print(my_array)                              # [1, 2, 4]

# delete the element at index 1 from a list
del my_array[1]
print(my_array)                              # [1, 4]

# delete the elements at index 0 and 1 from a list
del my_array[0:2]
print(my_array)                              # []

# ----------------------------------------------------------------

list = ["efg", "abc", "def", "gfg"]

print(max(list))                             # "gfg"
print(min(list))                             # "abc"

list.sort()
print(list)                                  # ["abc", "def", "efg", "gfg"]

list.reverse()
print(list)                                  # ["gfg", "efg", "def", "abc"]

# ----------------------------------------------------------------