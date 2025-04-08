# Count digits in a number

# I/P: 12345
# O/P: 5

# I/P: 123456789
# O/P: 9

# I/P: 10000
# O/P: 5

# ----------------------------------------------------------------

n = int(input("Enter a number: "))

count = 0

while n > 0:
    n = n // 10
    count += 1

print(count)






