# continue is used to skip the current iteration of the loop

# example:

# for i in range(1,10):
#     if i == 5:
#         continue    # skip the current iteration
#     print(i)
    
# ----------------------------------------------------------------

# Print all numbers in list that are not multiple of 5

l = [10, 25, 30, 45, 50, 60, 75, 80, 95, 100, 7, 13, 22, 31, 44]  # Added some non-multiples of 5

for i in l:
    if i%5 == 0:
        continue
    print(i)
    
# ----------------------------------------------------------------
