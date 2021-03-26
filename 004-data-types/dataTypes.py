# str
x = "Hello World"
x = str("Hello World")


# int
x = 20
x = int(20)

# float
x = 20.5
x = float(20.5)

# complex
x = 1j
x = complex(1j)


# list
colors = ["red", "green", "blue"]
colors = list(("red", "green", "blue"))

# tuple
colors = ("red", "green", "blue")
colors = tuple(("red", "green", "blue"))

# range
range(6)


# dict
record = {"name" : "John", "age" : 36}
record = dict(name="John", age=36)


# set
colors = {"red", "green", "blue"}
colors = set(("red", "green", "blue"))

# frozenset
colors = frozenset({"red", "green", "blue"})


# bool
x = True
y = False

x = bool(5)


print()

# bytes
x = b"Hello"
print("bytes:")
print(x)

x = bytes(10)
print("bytes:")
print(x)

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 65]
print("bytes:")
print(bytes(mylist))


# bytearray
x = bytearray(10)
print("bytearray:")
print(x)

# memoryarray
x = memoryview(bytes(5))
print("memoryview:")
print(x)

# random bytearray
someArray = bytearray('XYZ', 'utf-8')
print('Before:', someArray)

mv = memoryview(someArray)

# update 1st index of mv to Z
mv[1] = 90
print('After:', someArray)


# knowing type of data
x = 5
print()
print(type(x))
print()



# explicit typing
y = 20.5
x = int(y)   # x = 20


# strong typing
x = "123"
y = 2
print(x * y)