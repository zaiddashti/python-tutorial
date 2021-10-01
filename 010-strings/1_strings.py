# single quotations
print('This is a string with single quotations and uses "double" quotations within it')


# double quotations
print("This is a string with double quotations and uses 'single' quotations within it")


# assign variable to a string
singleQ = 'This is a string with single quotations'
print(singleQ)
doubleQ = "This is a string with double quotations"
print(doubleQ)


# multi-lines string with single quotations
singleQM = '''This is
a multi
line string
with single quotations'''
print(singleQM)


# multi-lines string with double quotations
doubleQM = """This is
a multi
line string
with double quotations"""
print(doubleQM)


# string to arrays
print(singleQ[3])


# looping through string array
for s in singleQ:
    print(s)


# string length
lengthOfSingleQ = len(singleQ)
print('The length of "' + singleQ + '" is ' + str(lengthOfSingleQ))


# check for a given string is in another string
print("with" in singleQ)

# using if statement
if "with" in singleQ:
    print("with is in '" + singleQ + "'")


# check for a given string is not in another string
print("test" not in singleQ)

# using if statement
if "test" not in singleQ:
    print("test is not in '" + singleQ + "'")


x = "The tall of the building is 30 meters"
print(x[28])
