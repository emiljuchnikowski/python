tuple1 = (1, 2, 3, 4)
tuple2 = ('a', 'b', 'c', 'd')
tuple3 = (True, False, True, False)
tuple4 = (1, 'a', True, 3.14)

print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)

x, y, z, w = tuple1
print(x)
print(y)
print(z)

user = {
    (1, 2): "Coordinates",
    (3, 4): "Another Coordinates"
}

print(user)
print(user[(1, 2)])  # Access value by key
print(user.get((3, 4)))  # Access value by key using get method
print(user.get((5, 6), "Not found"))  # Access with default value
