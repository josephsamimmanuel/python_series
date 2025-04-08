# Pyramid pattern in python

for i in range(1, 6):  # 5 rows for a nice pyramid
    # Print spaces
    for j in range(5 - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    print()  # New line after each row

# ----------------------------------------------------------------

n = int(input("Enter the number of rows: "))

for i in range(1, n+1):  
    # Print spaces
    for j in range(n - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    print()  # New line after each row