set1 = {1, 2, 3, 4,4,2}
set2 = {'a', 'b', 'c', 'd'}
set3 = {True, False}
set4 = {1, 'a', True, 3.14}

print(set1)
set1.add(5)  # Add element to the set
print(set1)
set1.add(5) # Adding duplicate element has no effect
print(set1)
set1.remove(3)  # Remove element from the set
print(set1)

print(len(set1))  # Length of the set
print(2 in set1)  # Check if element is in the set
print(10 not in set1)  # Check if element is not in the set
print(list(set1))  # Convert set to list

print(set1.difference(set4))
print(set1 & set4)  # Intersection
print(set1 | set4)  # Union
print(set1 ^ set4)  # Symmetric difference
set1.update({6, 7, 8})  # Update set with multiple elements
print(set1)
set1.clear()  # Clear the set
print(set1)
