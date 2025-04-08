# Prime number
# STEPS:
# 1. Get the input from the user
# 2. Run a loop from 2 to n - range(2, n)
# 3. Check if the current number divides n without remainder - if n % i == 0
# 4. If yes, print "Not a prime number" and break the loop - print("Not a prime number") and break
# 5. If no, continue the loop - continue
# 6. If the loop completes without breaking, print "Prime number" - else: print("Prime number")

n = int(input("Enter a number: "))

# Method 1: Using for loop

for i in range(2, n):
    if n % i == 0:
        print("Not a prime number")
        break
else:
    print("Prime number")
    
# ----------------------------------------------------------------

# Method 2: Using while loop

i = 2   

while i < n:
    if n % i == 0:
        print("Not a prime number")
        break
    i += 1
else:
    print("Prime number")   

# ----------------------------------------------------------------

# Method 3: Using recursion

def is_prime(n, i=2):
    if n <= 2:
        return True
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)

