dictionary = {
    "hello": "A greeting or expression of goodwill.",
    "world": "The earth or globe; the planet we live on.",
    "number": 123
}

print(dictionary)
print(dictionary["hello"])  # Access value by key
print(dictionary.get("world"))  # Access value by key using get method
print(dictionary.get("nonexistent", "Not found"))  # Access with default value

dictionary2 = dict(name = "Alice", age = 30, city = "New York")
print(dictionary2)
print('name' in dictionary2)  # Check if key exists
print('country' not in dictionary2)  # Check if key does not exist
print(len(dictionary2))  # Length of the dictionary
dictionary2["age"] = 31  # Update value
print(dictionary2)
dictionary2["country"] = "USA"  # Add new key-value pair
print(dictionary2)
del dictionary2["city"]  # Remove key-value pair
print(dictionary2)
popped_value = dictionary2.pop("age")  # Remove key and return its value
print(popped_value)
print(dictionary2)
print(dictionary2.keys())  # Get all keys
print(dictionary2.values())  # Get all values
print(dictionary2.items())  # Get all key-value pairs
dictionary2.update({"city": "Los Angeles", "age": 32})  # Update multiple key-value pairs
print(dictionary2)
