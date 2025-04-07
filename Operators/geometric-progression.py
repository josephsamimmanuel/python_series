# Geometric Progression

# a, ar, ar^2, ar^3, ...

# a is the first term
# r is the common ratio

# ----------------------------------------------------------------

# nth term of a geometric progression
# an = a * r^(n-1)

# sum of first n terms of a geometric progression
# Sn = a * (1-r^n) / (1-r)

# ----------------------------------------------------------------
# Example:
# a = 2, r = 3, n = 5
# an = 2 * 3^(5-1) = 2 * 81 = 162
# Sn = 2 * (1-3^5) / (1-3) = 2 * (1-243) / (-2) = 2 * 242 / 2 = 242

# ----------------------------------------------------------------

# Example:
# A person gets 5000 salary on 1st August 2020. This salary doubles every year.
# Find the salary on 1st August 2030.

# a = 5000
# r = 2
# n = 1st August 2030 - 1st August 2020 = 10 years
# an = 5000 * 2^(10-1) = 5000 * 512 = 2560000

# ----------------------------------------------------------------

# I/P : a = 2, r = 2, n = 10
# O/P : an = 2 * 2^(10-1) = 2 * 512 = 1024
#       Sn = 2 * (1-2^10) / (1-2) = 2 * (1-1024) / (-1) = 2 * 1023 = 2046

a = int(input("Enter the first term: "))
r = int(input("Enter the common ratio: "))
n = int(input("Enter the number of terms: "))

an = a * r**(n-1)
Sn = a * (1-r**n) / (1-r)

print(f"The {n}th term of the geometric progression is {an}")
print(f"The sum of the first {n} terms of the geometric progression is {Sn}")

# ----------------------------------------------------------------















