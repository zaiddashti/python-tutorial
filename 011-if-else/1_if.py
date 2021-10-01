# if statement
x = input("Enter the value of x: ")
y = input("Enter the value of y: ")

if x > y: # string comparisons
    print("The value of x is greater than the value of y")

if int(x) > int(y): # int comparisons
    print("The value of x is greater than the value of y")


# Syntax error because of indention
#if x > y:
#print("The value of x is greater than the value of y")


# multiple conditions
x = input("Enter the value of x: ")
y = input("Enter the value of y: ")
z = input("Enter the value of z: ")

if int(x) > int(y) and int(y) > int(z):
    print("The value of x is greater than the value of z")

if int(x) > int(y) or int(y) > int(z):
    print("The expressions x > y or y > z is satisfied.")


# check whether an item is in the list
x = input("Enter the value of x: ")
mylist = [1, 3, 5, 7, 9, 10]
if int(x) in mylist:
    print(str(x) + " is in the list [1,3,5,7,9,10]")

if x in mylist:    # "x in mylist" evaluated False since x is str and elements of mylist are int, so x is not in mylist
    print(str(x) + " is in the list [1,3,5,7,9,10]")

mylist2 = [1, 3, 5, 7, 9, 10, "55"]
if x in mylist2:
    print(str(x) + " is in the list [1,3,5,7,9,10]")




x = 20
y = 10

# short if example 1
if x > y: print("x is greater than y")

# short if example 2
print("x > y is True") if x > y else print("x > y is False")


# pass statement
if x > y:
  pass


# check whether the list is empty
myList = []
if myList:
    print("The list is not empty")
else:
    print("The list is empty")
