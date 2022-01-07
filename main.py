# Write a program to sort a list of names in alphabetical order and print the sorted list in uppercase
l=["apple","zebra","sachin","buck"]
l.sort()
print(l)
c = [x.upper() for x in l]

print(c)