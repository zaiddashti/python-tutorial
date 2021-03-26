# string concatenation using "+"
welcomeStr = "Hello, "
name = "Zaid"
print(welcomeStr + name + "!")


# + as concatenation with static string
print ("Welcome, " + name)


# + as concatenation with two variables
print(welcomeStr + name)


# + as addition operator
a = 1
b = 2
print(a+b)


# + between string and numbers gives error unless it is casted
#print(a + name)     # error since a is not string and need to be type casted
#print(name + b)     # error since b is not string and need to be type casted
print(str(a) + name)
print(name + str(b))
