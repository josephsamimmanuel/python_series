# Set in python

# Set is a collection of items that are unordered and mutable.
# Set is defined using curly braces.
# Set can contain different types of data.
# Set is indexed from 0.

# Creating a set
s1 = {1, 2, 3, 4, 5}
print(s1)                              # {1, 2, 3, 4, 5}

s2 = set([5,4,3,2,1,"Hello"])
print(s2)                              # {1, 2, 3, 4, 5, 'Hello'}

s9 = set ((1,2,3,4,5))
print(s9)                              # {1, 2, 3, 4, 5}

s3 = set("Hello")
print(s3)                              # {'H', 'e', 'l', 'o'}

s4 = set()
print(s4)                              # set()
print(type(s4))                        # <class 'set'>

s5 = {}
print(s5)                              # {}
print(type(s5))                        # <class 'dict'>

s6 = set(range(1, 10))
print(s6)                              # {1, 2, 3, 4, 5, 6, 7, 8, 9}

s7 = set(range(1, 10, 2))
print(s7)                              # {1, 3, 5, 7, 9}

# ----------------------------------------------------------------

# Set methods   

# add()

s10 = {1, 2, 3, 4, 5}
s10.add(6)
print(s10)                              # {1, 2, 3, 4, 5, 6}

# update()

s11 = {1, 2, 3, 4, 5}
s11.update([6, 7, 8, 9, 10])
print(s11)                              # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

s11.update({60,70}, [80,90,100])
print(s11)                              # {60, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 70, 80, 90, 100}

# remove()

s12 = {1, 2, 3, 4, 5, 60}
s12.remove(60)
print('After removing 60:',s12)                              # {1, 2, 3, 4, 5}

# discard()

s13 = {1, 2, 3, 4, 5, 60}
s13.discard(60)
print('After discarding 60:',s13)                              # {1, 2, 3, 4, 5}

# pop()

s14 = {1, 2, 3, 4, 5}
s14.pop()
print('After popping:',s14)                              # {2, 3, 4, 5}

# clear()

s15 = {1, 2, 3, 4, 5}
s15.clear()
print('After clearing:',s15)                              # set()

# copy()

s16 = {1, 2, 3, 4, 5}
s16.copy()
print('After copying:',s16)                              # {1, 2, 3, 4, 5}

# difference() - present in set1 but not in set2

s17 = {1, 2, 3, 4, 5}
s18 = {6, 7, 8, 9, 10}
s17.difference(s18)
print('After difference:',s17)                              # {1, 2, 3, 4, 5}

# difference_update() - present in set1 but not in set2

s19 = {1, 2, 3, 4, 5}
s20 = {6, 7, 8, 9, 10}
s19.difference_update(s20)
print('After difference_update:',s19)                              # {1, 2, 3, 4, 5}

# intersection() - present in both set1 and set2

s21 = {1, 2, 3, 4, 5}
s22 = {6, 7, 8, 9, 10}
s21.intersection(s22)
print('After intersection:',s21)                              # {1, 2, 3, 4, 5}

# intersection_update() - present in both set1 and set2

s23 = {1, 2, 3, 4, 5}
s24 = {6, 7, 8, 9, 10}
s23.intersection_update(s24)
print('After intersection_update:',s23)                  # set()

# isdisjoint() - no common elements

s25 = {1, 2, 3, 4, 5}
s26 = {6, 7, 8, 9, 10}
s25.isdisjoint(s26)
print('After isdisjoint:',s25)                              # {1, 2, 3, 4, 5}

# issubset() - all elements of set1 are present in set2

s27 = {1, 2, 3, 4, 5}
s28 = {6, 7, 8, 9, 10}
s27.issubset(s28)
print('After issubset:',s27)                                # {1, 2, 3, 4, 5}

# issuperset() - all elements of set2 are present in set1

s29 = {1, 2, 3, 4, 5}
s30 = {6, 7, 8, 9, 10}
s29.issuperset(s30)
print('After issuperset:',s29)                              # {1, 2, 3, 4, 5}

# symmetric_difference() - present in set1 or set2 but not in both

s31 = {1, 2, 3, 4, 5}
s32 = {6, 7, 8, 9, 10}
s31.symmetric_difference(s32)
print('After symmetric_difference:',s31)                    # {1, 2, 3, 4, 5}

# symmetric_difference_update() - present in set1 or set2 but not in both

s33 = {1, 2, 3, 4, 5}
s34 = {6, 7, 8, 9, 10}
s33.symmetric_difference_update(s34)
print('After symmetric_difference_update:',s33)             # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# union() - present in set1 or set2 or both

s35 = {1, 2, 3, 4, 5}
s36 = {6, 7, 8, 9, 10}
s35.union(s36)
print('After union:',s35)                                  # {1, 2, 3, 4, 5}

# update() - present in set1 or set2 or both

s37 = {1, 2, 3, 4, 5}
s38 = {6, 7, 8, 9, 10}
s37.update(s38)
print('After update:',s37)                                  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# ----------------------------------------------------------------

set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 9, 10}

# Union
print(set1 | set2)                                      # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print(set1.union(set2))                                  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Intersection
print(set1 & set2)                                      # set()

print(set1.intersection(set2))                          # set()

# Difference - present in set1 but not in set2
print(set1 - set2)                                      # {1, 2, 3, 4, 5}

print(set1.difference(set2))                            # {1, 2, 3, 4, 5}

# Symmetric Difference - present in set1 or set2 but not in both
print(set1 ^ set2)                                      # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print(set1.symmetric_difference(set2))                  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# issubset() - subset means all elements of set1 are present in set2
print(set1.issubset(set2))                              # False

# issuperset() - superset means all elements of set2 are present in set1
print(set1.issuperset(set2))                              # False

# isdisjoint() - no common elements
print(set1.isdisjoint(set2))                              # True

# <= - subset means all elements of set1 are present in set2  
print(set1 <= set2)                                      # False

# < - subset means all elements of set1 are present in set2 | proper subset - all elements of set1 are present in set2 but not equal to set2
print(set1 < set2)                                       # False

# >= - superset means all elements of set2 are present in set1
print(set1 >= set2)                                      # False

# > - superset means all elements of set2 are present in set1
print(set1 > set2)                                       # False

# ----------------------------------------------------------------


