x = 10
y = 2
z = 8

print("x = " + str(x))  # + is concatination and not addition, will be explained later
print("y = " + str(y))
print("z = " + str(z))


# addition
a = x + y
print("a = x + y = " + str(a))

y = y + 3   # y = 2 (old value) + 3 = 5 (new value)
print("y = y + 3 = " + str(y))


# subtraction
print("z - y = " + str(z - y))    # evaluate then print result. z = 8, y = 5 (new value), z - y = 3


# multiplication
print("x * y = " + str(x * y))


# division
print("x / y = " + str(x / y))
print("5 / 2 = " + str(5 / 2))
# floor division
print("5 // 2 = " + str(5 // 2))

# modulo (remainder of division)
print("x % z = " + str(x % z))


# exponentiation
print("x ** y = " + str(x ** y))
