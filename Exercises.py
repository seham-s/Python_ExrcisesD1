# Exercise 6
numbers = {2, 5, 16, 8, 7, 9, 3, 1}
# your code here
print(4 in numbers)
numbers.add(5) # duplicate element and will have no impact and the output will
print(numbers)
numbers.remove(5)
print(numbers)
# Find the maximum number in the set
m = max(numbers)
# Create a new set that contains numbers from m+1 to m+10
new_numbers = {n for n in range(m+1, m+11)}

# Print the original set
print(numbers)
# Create a set that is the union of the two sets
union_set = numbers.union(new_numbers)

# Print the union of the two sets
print(union_set)
# Create a set that is the union of the two sets
union_set = numbers.union(new_numbers)

# Print the union of the two sets
print(union_set)