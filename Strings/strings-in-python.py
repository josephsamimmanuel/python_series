# strings in python

# strings are immutable
# strings are ordered
# strings are indexed
# strings are iterable

# sequence of characters
# used to store text data like names, sentences, etc.
# Typically small set of characters
# Characters A to Z are stored in the memory as ASCII values from 65 to 90
# Characters a to z are stored in the memory as ASCII values from 97 to 122

#----------------------------------------------------------

print(ord("A")) # 65
print(ord("B")) # 66
print(ord("C")) # 67
print(ord("D")) # 68
print(ord("E")) # 69
print(ord("F")) # 70
print(ord("G")) # 71
print(ord("H")) # 72
print(ord("I")) # 73
print(ord("J")) # 74
print(ord("K")) # 75
print(ord("L")) # 76
print(ord("M")) # 77
print(ord("N")) # 78
print(ord("O")) # 79
print(ord("P")) # 80
print(ord("Q")) # 81
print(ord("R")) # 82
print(ord("S")) # 83
print(ord("T")) # 84
print(ord("U")) # 85
print(ord("V")) # 86
print(ord("W")) # 87
print(ord("X")) # 88
print(ord("Y")) # 89
print(ord("Z")) # 90


print(ord("a")) # 97
print(ord("b")) # 98
print(ord("c")) # 99
print(ord("d")) # 100
print(ord("e")) # 101
print(ord("f")) # 102
print(ord("g")) # 103
print(ord("h")) # 104
print(ord("i")) # 105
print(ord("j")) # 106
print(ord("k")) # 107
print(ord("l")) # 108
print(ord("m")) # 109
print(ord("n")) # 110
print(ord("o")) # 111
print(ord("p")) # 112
print(ord("q")) # 113
print(ord("r")) # 114
print(ord("s")) # 115
print(ord("t")) # 116
print(ord("u")) # 117
print(ord("v")) # 118
print(ord("w")) # 119
print(ord("x")) # 120
print(ord("y")) # 121
print(ord("z")) # 122

print(chr(65)) # A
print(chr(66)) # B
print(chr(67)) # C
print(chr(68)) # D
print(chr(69)) # E
print(chr(70)) # F

print(chr(97)) # a
print(chr(98)) # b
print(chr(99)) # c
print(chr(100)) # d
print(chr(101)) # e
print(chr(102)) # f

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
# string = "hello world"
# string.join(" ")
# Output: "hello world"

# 16. len() - returns the length of the string
# Example:
# string = "hello world"
# len(string)
# Output: 11

# 17. lower() - converts the string to lowercase
# Example:
# string = "Hello World"
# string.lower()
# Output: "hello world"

# 18. upper() - converts the string to uppercase
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
# string = "hello world"
# string.strip()
# Output: "hello world"

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
















