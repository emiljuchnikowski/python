is_true = True
is_licensed = True

if is_true and is_licensed:
    print("It's true!")
    print("This is still part of the if block")
elif is_licensed:
    print("It's licensed!")
    print("This is still part of the elif block")
else:
    print("It's false!")
    print("This is still part of the else block")

if is_true or is_licensed:
    print("It's true!")

print("This is outside the if-else block")

is_friend = False
can_message = "is true" if is_friend else "is false"
print(can_message)

print(is_true and is_licensed)

# operators
print(3 < 1) # False
print(4 == 5) # False
print(True == "test") # False
print('a' > 'b') # False
print('a' > 'A') # True
print(not True) # False

if (1 > 2) or True:
    print("Done")

print(1 == True) # True
print(1 is True) # False
