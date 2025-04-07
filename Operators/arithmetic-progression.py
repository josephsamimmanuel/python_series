# Arithmetic Progression

# a, a+d, a+2d, a+3d, ...

# a is the first term
# d is the common difference

# ----------------------------------------------------------------

# nth term of an arithmetic progression
# an = a + (n-1)d

# sum of first n terms of an arithmetic progression
# Sn = n/2 * (2a + (n-1)d)

# ----------------------------------------------------------------

# Example:
# a = 2, d = 3, n = 5
# an = 2 + (5-1) * 3 = 14
# Sn = 5/2 * (2*2 + (5-1)*3) = 5/2 * (4 + 12) = 5/2 * 16 = 40

# Example:
# A person gets 5000 salary on 1st August 2020. This salary increases by 2000 every month.
# Find the salary on 1st August 2025.

# a = 5000
# d = 2000
# n = 1st August 2025 - 1st August 2020 = 61 months
# an = 5000 + (61-1) * 2000 = 5000 + 120000 = 125000

# ----------------------------------------------------------------

# Example:

# I/P : a =5, d=2 , n=5

# O/P : an = 5 + (5-1) * 2 = 5 + 8 = 13
#       Sn = 5/2 * (2*5 + (5-1)*2) = 5/2 * (10 + 8) = 5/2 * 18 = 45

# I/P : a =10, d=10 , n=101
# O/P : an = 10 + (101-1) * 10 = 10 + 1000 = 1010
#       Sn = 101/2 * (2*10 + (101-1)*10) = 101/2 * (20 + 1000) = 101/2 * 1020 = 51510

a = int(input("Enter the first term: "))
d = int(input("Enter the common difference: "))
n = int(input("Enter the number of terms: "))

an = a + (n-1) * d
Sn = n/2 * (2*a + (n-1)*d)

print(f"The {n}th term of the arithmetic progression is {an}")
print(f"The sum of the first {n} terms of the arithmetic progression is {Sn}")

# ----------------------------------------------------------------




