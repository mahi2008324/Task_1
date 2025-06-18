# This code finds the product of all elements in the sublists that have the smallest length.
#finding out the smallest list element in the list then multiplying that elements
l = [[1,2,3,4],[5,6,7,8],[9,10],[11,12,13,14,5]]

# Find the length of the smallest sublist
smallest_length = len(l[0])
for sublist in l:
    if len(sublist) < smallest_length:
        smallest_length = len(sublist)

# Multiply the elements of all sublists with the smallest length
product = 1
for sublist in l:
    if len(sublist) == smallest_length:
        for item in sublist:
            product *= item

print("Product of elements in the smallest sublists:", product)

largest_length = len(l[0])
for sublist in l:
    if len(sublist) > largest_length:
        largest_length = len(sublist)
#sum of the elements in the largest sublist
sum_of_largest = 0
for sublist in l:
    if len(sublist) == largest_length:
        sum_of_largest += sum(sublist)

print("Sum of elements in the largest sublists:", sum_of_largest)