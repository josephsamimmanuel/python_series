# Loops in Python

# For Loop

for i in range(10):
    print(i)
    
# ----------------------------------------------------------------

# While Loop

i = 0
while i < 10:
    print(i)
    i += 1

# ----------------------------------------------------------------

# Nested Loop

for i in range(10):
    for j in range(10):
        print(i, j)

# ----------------------------------------------------------------


# Break Statement

for i in range(10):
    if i == 5:
        break
    print(i)

# ----------------------------------------------------------------

# Continue Statement

for i in range(10):
    if i == 5:
        continue
    print(i)

# ----------------------------------------------------------------

# Pass Statement

for i in range(10):
    pass

# ----------------------------------------------------------------

# For Loop with else

for i in range(10):
    print(i)
else:
    print("Loop ended")

# ----------------------------------------------------------------

# While Loop with else

i = 0
while i < 10:
    print(i)
    i += 1
else:
    print("Loop ended")

# ----------------------------------------------------------------

# For Loop with else

for i in range(10):
    print(i)
    if i == 5:
        break
else:
    print("Loop ended")

# ----------------------------------------------------------------

# Example
#Write a program to print table of a number

# I/P: n = 3
# O/P: 3 6 9 12 15 18 21 24 27 30

# I/P: n = 5
# O/P: 5 10 15 20 25 30 35 40 45 50

n = int(input("Enter a number: "))
m = int(input("Enter the range: "))

for i in range(1, m+1): 
    print(f"{i} x {n} = {n * i}")

# ----------------------------------------------------------------

# Example
#Write a program to print table of a number in reverse order

# I/P: n = 3
# O/P: 30 27 24 21 18 15 12 9 6 3

# I/P: n = 5
# O/P: 50 45 40 35 30 25 20 15 10 5

n = int(input("Enter a number: "))
m = int(input("Enter the range: "))

for i in range(m, 0, -1):  # range(start, stop, step)
    print(f"{i} x {n} = {n * i}")

# ----------------------------------------------------------------
