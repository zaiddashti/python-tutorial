# if-elif-else statement
x = input("Enter the value of x: ")
y = input("Enter the value of y: ")

if int(x) > int(y): # int comparisons
    print("The value of x is greater than the value of y")
elif int(x) == int(y):
    print("The value of x is equal to the value of y")
else:
    print("The value of x is less than the value of y")



# comparisons using multiple elif
x = input("Enter the value of x: ")
y = input("Enter the value of y: ")
z = input("Enter the value of z: ")

if int(x) > int(y): # int comparisons
    print("The value of x is greater than the value of y")
elif int(y) > int(z):
    print("The value of y is the greatest value")
elif int(y) < int(z):
    print("The value of y is the middle value")
else: # y == z
    print("The value of y is equal to the value of z")