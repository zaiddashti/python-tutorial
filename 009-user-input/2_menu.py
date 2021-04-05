# menu
print("Select one of the menu options:")
print("1) Add two numbers.")
print("2) Subtract two numbers.")
print("q) Quit the program.")

selected_option = input("Enter option [1,2,q]: ")

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
    print("Unknown option! Quiting...")

