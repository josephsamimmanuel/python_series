# Take a number from the user and print whether it is even or odd

n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# ----------------------------------------------------------------

x = int(input("Enter a number of coins: "))
y = input("Enter who starts the game: ")

if y == "Opponent":
    if x % 2 == 0:
        print("You are the Winner")
    else:
        print("Opponent is the Winner")
else:
    if x % 2 == 0:
        print("Opponent is the Winner")
    else:
        print("You are the Winner")

# ----------------------------------------------------------------


