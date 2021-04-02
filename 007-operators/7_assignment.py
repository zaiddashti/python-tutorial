# assign values to variables
x = 10

print("x = " + str(x))  # + is concatination and not addition, will be explained later

x += 5
print("After x += 5 => " + str(x))


x -= 2
print("After x -= 2 => " + str(x))


x *= 2
print("After x *= 2 => " + str(x))


x /= 2
print("After x /= 2 => " + str(x))


x //= 2
print("After x //= 2 => " + str(x))


x %= 4
print("After x %= 4 => " + str(x))


x **= 2
print("After x **= 2 => " + str(x))


x = int(x)  # we can't do bitwise operator on float, so we cast/convert it to int first
x &= 0
print("After x &= 0 => " + str(x))


x |= 1
print("After x |= 1 => " + str(x))


x ^= 2
print("After x ^= 2 => " + str(x))


x >>= 1
print("After x >>= 1 => " + str(x))


x <<= 1
print("After x <<= 1 => " + str(x))

print("==========")

# assign to multiple variables
x = y = z = 0
print("x = y = z = 0")
print("x = " + str(x))
print("y = " + str(y))
print("z = " + str(z))


x,y,z = 1,2,3
print("x,y,z = 1,2,3")
print("x = " + str(x))
print("y = " + str(y))
print("z = " + str(z))
