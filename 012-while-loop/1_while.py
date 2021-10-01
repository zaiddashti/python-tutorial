# print a line 10 time
index = 1

while index <= 10:
    print("Line " + str(index))
    index += 1

print("==========")


# while loop from 1 to 10
counter = 1

while counter <= 10:
    print(counter)
    counter += 1


print("==========")


# count from 1 to n

counter = 1
n = input("Enter an integer n: ")

while counter <= int(n):
    print(counter)
    counter += 1


print("==========")



# sum and average from 1 to n

counter = 1
sum = 0
n = input("Enter an integer n: ")

while counter <= int(n):
    sum += counter
    counter += 1
print("Sum from 1 to " + n + " is " + str(sum))
print("Average from 1 to " + n + " is " + str(sum/int(n)))


print("==========")


# factorial from 1 to n

counter = 1
n = input("Enter an integer n: ")
factorial = 1

while counter <= int(n):
    factorial *= counter
    counter += 1
print("Factorial " + n + " is " + str(factorial))


print("==========")


# break statement
counter = 1

while counter <= 10:
    if counter == 6:
        break
    print(counter)
    counter += 1


print("==========")


# continue statement: prints evens
counter = 1

while counter <= 10:
    if counter % 2 == 1:
        counter += 1
        continue
    print(counter)
    counter += 1


print("==========")


# while else loop from 1 to 10
counter = 1

while counter <= 10:
    print(counter)
    counter += 1
else:
    print("counter is beyond 10")


# user menu
selected_option = ""

while selected_option != "q":
    print()
    print("Select one of the menu options:")
    print("1) Add two numbers.")
    print("2) Subtract two numbers.")
    print("q) Quit the program.")

    selected_option = input("Enter option [1,2,q]: ")
    print()

    if selected_option == "1":
        x = input("Enter the first number: ")
        y = input("Enter the second number: ")
        print(x + " + " + y + " = " + str(int(x)+int(y)))
    elif selected_option == "2":
        x = input("Enter the first number: ")
        y = input("Enter the second number: ")
        print(x + " - " + y + " = " + str(int(x)-int(y)))
    elif selected_option == "q":
        print("Quiting...")
    else:
        print("Unknown option!")
    

