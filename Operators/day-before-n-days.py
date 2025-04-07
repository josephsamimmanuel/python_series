# Day before n days

# Example:
# I/P : d = 1
# I/P : n = 1
# O/P : 0   Sunday

# I/P : d = 0
# I/P : n = 9
# O/P : 5   Friday

# I/P : d = 1
# I/P : n = 3
# O/P : 5   Friday

# I/P : d = 1
# I/P : n = 10
# O/P : 5   Friday

# Day before n days
# (d-n) % 7

# ----------------------------------------------------------------  

d = int(input("Enter the day: "))
n = int(input("Enter the number of days: "))
day_before = (d-n) % 7
print(f"The day before {n} days is {day_before}")

# ----------------------------------------------------------------



