for item in 'Hello World':
    print(item)

for number in range(5):
    print(number)

for number in (3, 8):
    print(number)

for number in [2, 4, 6, 8]:
    print(number)

for number in {1, 3, 5, 7}:
    print(number)
print(number)

for key in {'a': 1, 'b': 2}:
    print(key)
    print({'a': 1, 'b': 2}[key])

my_list = [1, 2, 3]
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")

condition = 0
while condition < 5:
    print(condition)
    condition += 1
else:
    print("Condition is no longer less than 5")

for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # This will print only odd numbers

for i in range(5):
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)  # This will print 0, 1, 2

for i in range(5):
    pass  # Placeholder, does nothing. Is used to avoid syntax errors in empty loops

