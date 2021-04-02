# After first or is not evaluated since we have True or, then no need to evaluate the rest
expr1 = True or False and True and True and False or False
print("expr1 = " + str(expr1))



# Since it is all "and", the expression after "False" is not evaluated
expr2 = True and True and False and True and True
print("expr2 = " + str(expr2))

