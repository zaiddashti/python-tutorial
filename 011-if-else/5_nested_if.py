# nested if statements
x = 10
if x > 0:
    if x > 10:
        print("x is positive and greater than 10")
    else:
        print("x is positive between 0 and 10")
else:
    print("x is negative")



# find whether x is positive/negative and odd/even
x = input("Enter the value of x: ")

if int(x) > 0: 
    if int(x)%2 == 0:
        print("x is positive even")
    else:
        print("x is positive odd")
elif int(x) == 0:
    print("The value of x is 0")
else:
    if (-int(x))%2 == 0:
        print("x is negative even")
    else:
        print("x is negative odd")




# get 3 numbers and print them in ascending order
x = input("Enter the value of x: ")
z = input("Enter the value of y: ")
y = input("Enter the value of z: ")

if int(x) <= int(y):
    if int(y) <= int(z):
        print(x + ", " + y + ", " + z)
    else:
        if int(x) <= int(z):
            print(x + ", " + z + ", " + y)
        else:
            print(z + ", " + x + ", " + y)
else:
    if int(y) >= int(z):
        print(z + ", " + y + ", " + x)
    else:
        if int(x) >= int(z):
            print(y + ", " + z + ", " + x)
        else:
            print(y + ", " + x + ", " + z)