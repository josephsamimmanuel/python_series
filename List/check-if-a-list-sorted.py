# check if a list is sorted

print("Enter the list of elements: ")
l = list(map(int, input().split()))

if l == sorted(l):
    print("List is sorted")
else:
    print("List is not sorted")

