# Given an integer s, write a program to print the square of size s using "*" character. 
# Note: Make sure to add a " " between two "*". Add a new line after printing the square
# Expected Output:
# * * * *
# *     *
# *     *
# * * * *

s = int(input("Enter the size of the square: "))

# Print the top row
print("* " * s)

# Print the middle rows
for i in range(s - 2):
    print("*" + " " * (2 * (s - 2)) + " *")

# Print the bottom row (only if s > 1)
if s > 1:
    print("* " * s)

# ----------------------------------------------------------------

# EXPECTED OUTPUT:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

n = int(input("Enter the size of the square: "))

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

# ----------------------------------------------------------------

