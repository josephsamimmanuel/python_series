# break is used to terminate the loop

# example:

for i in range(1,10):
    if i == 5:
        break
    print(i)
    
# ----------------------------------------------------------------

# Find the smallest divisor of a number such that the divisor is greater than 1

n = int(input("Enter a number: "))

for i in range(2,n+1):
    if n%i == 0:
        print(f"The smallest divisor of {n} is {i}")
        break # break the loop if the condition is true
    
# ----------------------------------------------------------------

# Find the greatest divisor of a number such that the divisor is greater than 1

n = int(input("Enter a number: "))

for i in range(n, 1, -1):  # Start from n and go down to 2
    if n % i == 0:
        print(f"The greatest divisor of {n} is {i}")
        break  # Now we can break after finding the first (largest) divisor

# ----------------------------------------------------------------
