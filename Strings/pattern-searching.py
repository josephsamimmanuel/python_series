# Pattern Searching

# 1. Naive Pattern Searching
# 2. KMP Algorithm
# 3. Rabin Karp Algorithm
# 4. Boyer Moore Algorithm
# 5. Z Algorithm
# 6. Aho Corasick Algorithm
# 7. Knuth Morris Pratt Algorithm
# 8. Finite Automata
# 9. Suffix Tree
# 10. Suffix Array
# 11. Trie
# 12. Aho Corasick Algorithm

# ------------------------------------------------------------

text = input("Enter the text: ")       # geeks for geeks 
pattern = input("Enter the pattern: ") # geeks

pos = text.find(pattern)               # 0          10

while pos != -1:                       # 0 != -1    10 != -1     | -1 means not found
    print(pos)                         # 0          10
    pos = text.find(pattern, pos + 1)  # 0 + 1 = 1  10 + 1 = 11











