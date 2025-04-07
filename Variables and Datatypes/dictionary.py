# Dictionary is a collection of key-value pairs
# Dictionary is unordered
# Dictionary is mutable
# Dictionary is indexed by keys
# Values may be repeated
# Keys must be immutable
# Keys must be unique
# Keys must be hashable

# Creating a dictionary
d1 = {'name': 'John', 'age': 20, 'city': 'New York'}
print(d1)                              # {'name': 'John', 'age': 20, 'city': 'New York'}

# Accessing a dictionary
print(d1['name'])                     # John

# Adding a key-value pair
d1['email'] = 'john@gmail.com'
print(d1)                             # {'name': 'John', 'age': 20, 'city': 'New York', 'email': 'john@gmail.com'}

# Removing a key-value pair using del
del d1['age']
print(d1)                             # {'name': 'John', 'city': 'New York', 'email': 'john@gmail.com'}

# Removing a key-value pair using pop()
d1.pop('city')
print(d1)                             # {'name': 'John', 'email': 'john@gmail.com'}

# Removing a key-value pair using popitem()
d1.popitem()
print(d1)                             # {'name': 'John'}

# Removing all key-value pairs using clear()
d1.clear()
print(d1)                             # {}

# Deleting the dictionary using del
#del d1
#print(d1)                             # NameError: name 'd1' is not defined

# Creating a dictionary using dict()
d2 = dict(name='John', age=20, city='New York')
print(d2)                             # {'name': 'John', 'age': 20, 'city': 'New York'}

# Creating a dictionary using fromkeys()
d3 = dict.fromkeys(['name', 'age', 'city'], 'unknown')
print(d3)                             # {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}

# Creating a dictionary using fromkeys() with range
d4 = dict.fromkeys(range(1, 11), 'unknown')
print(d4)                             # {1: 'unknown', 2: 'unknown', 3: 'unknown', 4: 'unknown', 5: 'unknown', 6: 'unknown', 7: 'unknown', 8: 'unknown', 9: 'unknown', 10: 'unknown'}

# Creating a dictionary using fromkeys() with tuple
d5 = dict.fromkeys((1,2,3,4,5), 'unknown')  
print(d5)                             # {1: 'unknown', 2: 'unknown', 3: 'unknown', 4: 'unknown', 5: 'unknown'}

# Creating a dictionary using fromkeys() with tuple
d6 = dict.fromkeys((1,2,3,4,5), (1,2,3,4,5))  
print(d6)                             # {1: (1, 2, 3, 4, 5), 2: (1, 2, 3, 4, 5), 3: (1, 2, 3, 4, 5), 4: (1, 2, 3, 4, 5), 5: (1, 2, 3, 4, 5)}

# ------------------------------------------------------------------------------------------------

# Dictionary is unordered
d = { 110:'abc', 101:'def', 102:'ghi'}
print(d)                              # {110: 'abc', 101: 'def', 102: 'ghi'}

# Dictionary is mutable
d = {}
d["laptop"] = 40000
d["mobile"] = 30000
d["earphone"] = 20000
print(d)                              # {'laptop': 40000, 'mobile': 30000, 'earphone': 20000}

print(d["laptop"])                   # 40000

# ------------------------------------------------------------------------------------------------

dictionary = { 110:'abc', 101:'def', 102:'ghi'}

print(dictionary.get(101))            # def

print(dictionary.get(103))            # None

print(dictionary.get(103, "Not Found"))            # Not Found

if 101 in dictionary:
    print("Present")
else:
    print("Not Present")           # Present
    
# ------------------------------------------------------------------------------------------------

x = { '110':'abc', '101':'def', '102':'ghi'}

x[100] = 'xyz'
print(x)                              # {'110': 'abc', '101': 'def', '102': 'ghi', 100: 'xyz'}

print(len(x))                         # 4

x.pop(100)
print(x)                              # {'110': 'abc', '101': 'def', '102': 'ghi'}

x.popitem()
print(x)                              # {'110': 'abc', '101': 'def'}

##del x[102]
##print(x)                              # {'110': 'abc', '101': 'def'}

x.clear()
print(x)                              # {}

# ------------------------------------------------------------------------------------------------









