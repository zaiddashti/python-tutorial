# Output a message and take user input at the same time
name = input("Enter your name: ")

age = input("Enter your age: ")
age = int(age)

print()

print("Your name is: " + name)
print("Your age is: " + str(age))

print()

print("Variable 'name' is of type: " + str(type(name)))
print("Variable 'age' is of type: " + str(type(age)))




'''
# Using python v 2.7

name = raw_input("Enter your name: ")
print("Your name is: " + name)
'''
