# Get smaller element from list

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get smaller element from list
print(min(l)) # 1
print(max(l)) # 10

# ------------------------------------------------------------

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get smaller elements from list
x = 5
l1 = [i for i in l if i < x] # list comprehension - list of elements from l if i < x
print(l1) # [1, 2, 3, 4]



