li = [1, 2, 3, 4];
li2 = ['a', 'b', 'c', 'd'];
li3 = [True, False, True, False];
li4 = [1, 'a', True, 3.14];

print(li)
print(li2)
print(li3)
print(li4)

print(li[0])  # First element
print(li[-1]) # Last element
print(li[1:3]) # Slice from index 1 to 2
print(li[:2])  # First two elements
print(li[::2]) # Every second element
print(li[::-1]) # Reverse the list
print(li[2:])  # From index 2 to end
print(li[1:-1]) # From index 1 to second last element

print(len(li)) # Length of the list
li.append(5)   # Add element to the end
print(li)
li.insert(2, 2.5) # Insert element at index 2
print(li)
li.remove(3)  # Remove first occurrence of value 3
print(li)
popped = li.pop() # Remove and return last element
print(popped)
print(li)
li.sort()     # Sort the list
print(li)
print(sorted(li2)) # Return a sorted copy of the list
li.reverse()  # Reverse the list
print(li)
print(li.index(2)) # Index of first occurrence of value 2
print(li.count(2)) # Count occurrences of value 2
li2.extend(['e', 'f']) # Extend list with another list
print(li2)
print(li + li2) # Concatenate lists
print(li * 2)   # Repeat list
print(3 in li)  # Check if value is in list
print(10 not in li) # Check if value is not in list

print(list(range(5, 20))) # Create a list from a range


sentence = '!'
new_sentence = sentence.join(["hi", "hello", "there"])
print(new_sentence)

a,b,c, *other, d = [1,2,3, 4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(other)
print(d)
