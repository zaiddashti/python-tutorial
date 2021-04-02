x = 10
y = 5

print("x = " + str(x))  # + is concatination and not addition, will be explained later
print("y = " + str(y))


# and
result = x > 5 and y == 5
print("x > 5 and y == 5 = " + str(result))

result = x == 5 and y == 5
print("x == 5 and y == 5 = " + str(result))


# or
result = x < 5 or y == 5
print("x < 5 or y == 5 = " + str(result))

result = x == 5 or y == 5
print("x == 5 or y == 5 = " + str(result))

result = x == 5 or y > 5
print("x == 5 or y > 5 = " + str(result))


# not
result = not(x == 5)
print("not(x == 5) = " + str(result))