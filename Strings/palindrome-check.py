# 13. Palindrome Check

# ------------------------------------------------------------
# 13.1 Palindrome Check using string slicing
text = input("Enter the text: ")

if text == text[::-1]: # text[::-1] is the reverse of the text
    print("Palindrome")
else:
    print("Not a Palindrome")
    
# ------------------------------------------------------------
    
number = input("Enter the number: ")

if number == number[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

# ------------------------------------------------------------
# 13.2 Palindrome Check using loop
text = input("Enter the text: ")

for i in range(len(text)//2):
    if text[i] != text[-i-1]:
        print("Not a Palindrome")
        break
else:
    print("Palindrome")
    
# ------------------------------------------------------------
# 13.3 Palindrome Check using recursion
def is_palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])

text = input("Enter the text: ")

if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a Palindrome")
    
# ------------------------------------------------------------