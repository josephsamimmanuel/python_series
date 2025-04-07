# Bitwise Operators in Python

# & - AND
# | - OR
# ^ - XOR
# ~ - NOT
# << - LEFT SHIFT
# >> - RIGHT SHIFT

# & - AND - returns 1 if both the bits are 1
a = 10  # 00001010
b = 20  # 00010100
print(a & b)          # 0  # 00000000


# | - OR - returns 1 if one of the bits is 1 and the other is 0
a = 10  # 00001010
b = 20  # 00010100
print(a | b)          # 30  # 00011110

# ------------------------------------------------------------

# ^ - XOR - returns 1 if one of the bits is 1 and the other is 0
a = 10  # 00001010
b = 20  # 00010100
print(a ^ b)          # 30  # 00011110

# ------------------------------------------------------------

# ~ - NOT
a = 10  # 00001010
print(~a)          # -11  # 11110101

# ------------------------------------------------------------

# << - LEFT SHIFT - shifts the bits to the left
a = 10  # 00001010
print(a << 1)          # 20  # 00010100

a=5     # 00000101
print(a << 1)          # 10 # 00001010

# ------------------------------------------------------------

# >> - RIGHT SHIFT - shifts the bits to the right
a = 10  # 00001010
print(a >> 1)          # 5  # 00000101

a=5     # 00000101
print(a >> 1)          # 2 # 00000010

# ------------------------------------------------------------

print(~10)  # 00001010      -11     # 11110101
print(~-10) # 00001010      9       # 00001001
print(~0)   # 00000000      -1      # 11111111
print(~1)   # 00000001      -2      # 11111110
print(~-2)  # 00000010      1       # 00000001

# For negative numbers, the result is the two's complement of the number.

# BINARY REPRESENTATION OF 10 - 0000 1010 
# Bitwise NOT of 00001010 is    1111 0101 - THIS IS 2'S COMPLEMENT OF 11

# 11 - 0000 1011

# 1's complement - 1111 0100
# 2's complement - 1111 0101

# ------------------------------------------------------------

print(bin(18))          # 0b10010
print(bin(12))          # 0b1100
print(int("0b10010", 2))          # 18
print(int("0b1100", 2))          # 12

# ------------------------------------------------------------




