# count distinct elements in a list

print("Enter the list of elements: ")
l = list(map(int, input().split())) # split - split the input into a list

distinct_elements = len(set(l))     # set - remove duplicate elements

print(distinct_elements)
