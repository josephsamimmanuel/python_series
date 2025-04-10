# Separate even and odd numbers from list

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l1 = [i for i in l if i % 2 == 0] # i for i in l - for each element in l
l2 = [i for i in l if i % 2 != 0]

print(l1) # [2, 4, 6, 8, 10]
print(l2) # [1, 3, 5, 7, 9]

# ------------------------------------------------------------

