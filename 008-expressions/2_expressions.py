# Examples
x = 5.75		# of type float
print(type(x))

x = 40 > 30		# of type bool, value = True
print(type(x))

x = 2 + 4 // 2	# of type int, value = 4
print(type(x))

x = "Welcome"	# of type str
print(type(x))



# more examples on expressions
expr1 = 5 > 4 and 50 < 30
print("expr1 = " + str(expr1))


expr2 = 5 > 4 and 50 < 30 or True
print("expr2 = " + str(expr2))


x = 10
y = 5
z = 2
expr3 = x >= y and x % 2 == 1 or x / y == z
print("expr3 = " + str(expr3))