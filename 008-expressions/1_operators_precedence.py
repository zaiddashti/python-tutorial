# How to evaluate an expression:
# 1) Start with the highest precedence
# 2) If two operators have same priority, then start from left to right


# arithmetic operations

# Example 1
x = 2 + 4 // 2
print(x)

x = (2 + 4) // 2
print(x)


# Example 2
x = 2 + 3 * 4       # = 14
print(x)

y = (2 + 3) * 4     # = 20
print(y)



# conditions / boolean expression
expr1 = True or False and False
print("expr1 = " + str(expr1))

expr2 = (True or False) and False
print("expr2 = " + str(expr2))
