#Basic

print("Hello, World!")

# name = input("What is your name? ")

# print(f"Hello, {name}!")

#Fundamental Data types

##int
print(type(2 + 4))

#float
print(type(2 / 4))
print(type(5.00012))
print(2*3)
print(2**3)

#math functions
print(round(3.14159, 2))
print(abs(-7.25))

bool
str
list
tuple
set
dict

#Classes -> custom types

#Specialized data types
None

#Binary presentation
print(bin(5))
print(int("0b101", 2))

# Strings
print(type("hi hello there"))
usernam = "codeup"
print(usernam[0])
print(usernam[-1])
print(usernam[1:4])
print(usernam[:3])
print(usernam[1:3:2])
print(usernam[::-1]) # reverse string
print(usernam[3:])
print(usernam[1:-1])

print(len(usernam))
print(usernam.upper())
print(usernam.lower())
print(usernam.startswith("code"))
print(usernam.endswith("up"))
print(usernam.find("up"))
print(usernam.replace("up", "down"))
print("   hi   ".strip())
print("   hi   ".lstrip())
print("   hi   ".rstrip())
print(" ".join(["hi", "hello", "there"]))
print("hi hello there".split(" "))
print("hi hello there".count("h"))
print("hi hello there".index("e"))
print("hi hello there".capitalize())
print("hi hello there".title())
print(type(f"Hello, {usernam}!"))
print("Hello, {}!".format(usernam))
print("Hello, {0}!".format(usernam))
print("Hello, {name}!".format(name=usernam))
print("Hello, %s!" % usernam)
print("Hello, %s! You have %d new messages." % (usernam, 5))
print(type(str(123)))

# Booleans
print(type(True))
print(type(False))
print(1 == 1)
print(1 != 2)
print(1 > 2)
print(1 < 2)
print(1 >= 1)
print(1 <= 2)
print(True and False)
print(True or False)
print(not True)
print(not False)
print(bool(1))
print(bool(0))
print(bool(-1))
print(bool(""))
print(bool("hi"))
print(bool([]))
