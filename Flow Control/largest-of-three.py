# Take three numbers from the user and print the largest of the three
# if the numbers are equal, print all are equal

# Method 1:
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if a == b == c:
    print("All are equal")
elif a >= b and a >= c:
    print("a is the largest number")
elif b >= a and b >= c:
    print("b is the largest number")
else:
    print("c is the largest number")

# ----------------------------------------------------------------

# Method 2:

if a >= b:
    if a >= c:  
        print("a is the largest number")
    else:
        print("c is the largest number")
else:
    if b >= c:
        print("b is the largest number")
    else:
        print("c is the largest number")
        
# ----------------------------------------------------------------

# Method 3:

print(max(a, b, c))




