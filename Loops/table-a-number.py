# table of a number

n = int(input("Enter a number: "))
m = int(input("Enter the range:"))

for i in range(1,m+1):
    print(f"{n} x {i} = {n*i}")
    
# ----------------------------------------------------------------

# example:

n = int(input("Enter a number: "))
m = int(input("Enter the range:"))

i = 1

while i<=m:
    print(f"{n} x {i} = {n*i}")
    i += 1
    
# ----------------------------------------------------------------



