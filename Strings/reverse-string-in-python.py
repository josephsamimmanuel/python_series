# 13.1 Reverse String in Python using string slicing
text = input("Enter the text: ")

print(text[::-1]) # [::-1] is the reverse of the text

# ------------------------------------------------------------
# 13.2 Reverse String in Python using loop
text = input("Enter the text: ")

for i in range(len(text)-1, -1, -1):
    print(text[i], end="")

# ------------------------------------------------------------
