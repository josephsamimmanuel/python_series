s1 = "Hello"
s2 = "John"

print(s2 in s1) # False

print(s2 not in s1) # True

print(s1 == s2) # False

print(s1 != s2) # True

print(s1 > s2) # False because H is less than J

print(s1 < s2) # True because H is less than J

print(s1 >= s2) # False because H is less than J

print(s1 <= s2) # True because H is less than J

# ------------------------------------------------------------------------------------------------

s1 ="geeksforgeeks"
s2 = "geeks"

print(s1.index(s2)) # 0 - returns the index of the first occurrence of the substring

print(s1.find(s2)) # 0 - returns the index of the first occurrence of the substring

print(s1.rindex(s2)) # 8 - returns the index of the last occurrence of the substring

print(s1.rfind(s2)) # 8 - returns the index of the last occurrence of the substring

print(s1.index(s2, 1, 13)) # 8 - returns the index of the first occurrence of the substring in the range of the string | Takes start and end index as arguments

#----------------------------------------------------------

# string methods

# 1. capitalize() - converts the first character to uppercase
# Example:
# string = "hello world"
# string.capitalize()
# Output: "Hello world"

# 2. casefold() - converts the string to lowercase
# Example:
# string = "Hello world"
# string.casefold()
# Output: "hello world"

# 3. center() - centers the string to the specified width
# Example:
# string = "hello world"
# string.center(20)
# Output: "    hello world    "

# 4. count() - counts the number of occurrences of a substring in a string
# Example:
# string = "hello world"
# string.count("l")
# Output: 3

# 5. endswith() - checks if the string ends with the specified suffix
# Example:
# string = "hello world"
# string.endswith("world")
# Output: True

# 6. find() - finds the first occurrence of a substring in a string
# Example:
# string = "hello world"
# string.find("world")
# Output: 6

# 7. index() - finds the first occurrence of a substring in a string
# Example:
# string = "hello world"
# string.index("world")
# Output: 6

# 8. isalnum() - checks if the string is alphanumeric
# Example:
# string = "hello world"
# string.isalnum()
# Output: False

# 9. isalpha() - checks if the string is alphabetic
# Example:
# string = "hello world"
# string.isalpha()
# Output: False

# 10. isdigit() - checks if the string is numeric
# Example:
# string = "12345"
# string.isdigit()
# Output: True

# 11. islower() - checks if the string is lowercase
# Example:
# string = "hello world"
# string.islower()
# Output: True

# 12. isspace() - checks if the string is whitespace
# Example:
# string = "hello world"
# string.isspace()
# Output: False

# 13. istitle() - checks if the string is titlecased
# Example:
# string = "Hello World"
# string.istitle()
# Output: True

# 14. isupper() - checks if the string is uppercase
# Example:
# string = "HELLO WORLD"
# string.isupper()
# Output: True

# 15. join() - joins the elements of an iterable to the string
# Example:
# string = ["hello world", "geeksforgeeks", "python"]
# string.join(" ")
# Output: "hello world geeksforgeeks python"

# 16. len() - returns the length of the string
# Example:
# string = "hello world"
# len(string)
# Output: 11

# 17. lower() - converts the string to lowercase all
# Example:
# string = "Hello World"
# string.lower()
# Output: "hello world"

# 18. upper() - converts the string to uppercase all
# Example:
# string = "hello world"
# string.upper()
# Output: "HELLO WORLD"

# 19. replace() - replaces the specified substring with the new substring
# Example:
# string = "hello world"
# string.replace("hello", "hi")
# Output: "hi world"

# 20. split() - splits the string into a list of substrings
# Example:
# string = "hello world"
# string.split(" ")
# Output: ["hello", "world"]

# 21. strip() - removes the leading and trailing whitespace from the string
# Example:
# string = "---hello world---"
# string.strip("-")
# Output: "hello world"

# 21.1 lstrip() - removes the leading whitespace from the string
# Example:
# string = "---hello world---"
# string.lstrip("-")
# Output: "hello world---"

# 21.2 rstrip() - removes the trailing whitespace from the string
# Example:
# string = "---hello world---"
# string.rstrip("-")
# Output: "---hello world"





# 22. swapcase() - swaps the case of the string
# Example:  
# string = "Hello World"
# string.swapcase()
# Output: "hello world"

# 23. title() - converts the first character of each word to uppercase
# Example:
# string = "hello world"
# string.title()
# Output: "Hello World"

# 24. zfill() - pads the string with zeros to the specified width
# Example:
# string = "123"
# string.zfill(5)
# Output: "00123"

# 25. isdecimal() - checks if the string is decimal
# Example:
# string = "123"
# string.isdecimal()
# Output: True

# 26. isidentifier() - checks if the string is a valid identifier
# Example:
# string = "hello_world"
# string.isidentifier()
# Output: True

# 27. isprintable() - checks if the string is printable
# Example:
# string = "hello world"
# string.isprintable()
# Output: True

# 28. isspace() - checks if the string is whitespace
# Example:
# string = "hello world"
# string.isspace()
# Output: False

# 29. istitle() - checks if the string is titlecased
# Example:
# string = "Hello World"
# string.istitle()
# Output: True

# 30. isupper() - checks if the string is uppercase
# Example:
# string = "HELLO WORLD"
# string.isupper()
# Output: True

# 31. isspace() - checks if the string is whitespace
# Example:
# string = "hello world"
# string.isspace()
# Output: False

# 32. istitle() - checks if the string is titlecased
# Example:
# string = "Hello World"
# string.istitle()
# Output: True

# 33. startswith() - checks if the string starts with the specified prefix
# Example:
# string = "hello world"
# string.startswith("hello")
# Output: True




















