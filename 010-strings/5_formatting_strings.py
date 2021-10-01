# wrong usage of string since x is of type int
#x = 10
#strExample1 = "The number of coins is " + x
#print(strExample1)


# using format()
x = 10
strExample2 = "The number of coins is {}"    # {} is used to be replaced with x
print(strExample2.format(x))                 # replacing {} with x


# using format() with multiple arguments
x = 10
y = 20.5
z = 30j
strExample3 = "The value of x is {}, y is {}, z is {}."
print(strExample3.format(x, y, z))      # arguments are displayed in order


# formatting the orders in the string
strExample3 = "The value of y is {1}, z is {2}, x is {0}."
print(strExample3.format(x, y, z))      # arguments are displayed in order
