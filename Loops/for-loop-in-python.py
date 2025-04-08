# for loop is used to iterate over a sequence (list, tuple, string, dictionary, set, range) or other iterable objects.

# syntax:
# for i in range(start, stop, step):
#     body of the loop

# example:
# l = [10, 20, 30, 40, 50]

for i in [10, 20, 30, 40, 50]:
    print(i)    # similar to forEach loop in java

# ----------------------------------------------------------------

# example:
# name = "John"

for i in "John":
    print(i)

# ----------------------------------------------------------------

# example:
# range(5)

for i in range(5):
    print(i)

# ----------------------------------------------------------------

# example:

for i in range(20):
    if i%4 == 0:
        print(i)

# ----------------------------------------------------------------

# example:

l = [10, 20, 30, 40, 50]

for i in range(len(l)):
    print(l[i])

# ----------------------------------------------------------------

# example:

l = [10, 20, 30, 40, 50]

for i in range(len(l)):
    print(i, l[i])
    
# ----------------------------------------------------------------











