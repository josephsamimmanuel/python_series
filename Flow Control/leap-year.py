# Take a year from the user and print whether it is a leap year or not

# If the year is divisible by 4, go to step 2.
# If the year is divisible by 100, go to step 3.
# If the year is divisible by 400, then it's a leap year.
# Otherwise, it's not a leap year.

year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")

# ----------------------------------------------------------------

# Two people are born in same year 1948. In 2020, one person celebrates 72nd birthday and the other person celebrates 
# 18th birthday. how?

# Person 2 born on 29th February 1948.

# ----------------------------------------------------------------
