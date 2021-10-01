#  nested loops: multiplication schedule
print("i \tx \tj\t= \tr")
print("==================================")

i = 1
while i <= 10:
    j = 1
    while j <= 10:
        r = i * j
        print(str(i) + " \tx \t" + str(j) + " \t= \t" + str(r))
        j += 1
    i += 1


print("==================================")
# weeks and days
weeks = 4
daysPerWeek = 7

weekNumber = 1
while weekNumber <= weeks:
    print("Week: " + str(weekNumber))

    dayNumber = 1
    while dayNumber <= daysPerWeek:
        print("\t Day: " + str(dayNumber))
        dayNumber += 1

    weekNumber += 1


print("==================================")
# Triangle pattern
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''
size = 5

i = 1
while i <= size:

    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1

    print()
    i += 1

print("==================================")
# Triangle pattern
'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
'''
size = 5

i = 1
while i <= size:

    j = 1
    while j <= i:
        print(i, end=" ")
        j += 1

    print()
    i += 1



print("==================================")
# Triangle pattern
'''
      1 
    1 2 3 
  1 2 3 4 5 
1 2 3 4 5 6 7 
'''
size = 5

i = 1
while i <= size:

    j = 1
    while j <= size - i:
        print(" ", end=" ")
        j += 1

    j = 1
    while j <= i:
        print(j, end=" ") # replace j with i
        j += 1

    print()
    i += 1



print("==================================")
# Triangle pattern
'''
      1 
    1 2 3 
  1 2 3 4 5 
1 2 3 4 5 6 7 
'''
size = 5

i = 1
while i <= size:

    j = 1
    while j <= size - i:
        print(" ", end=" ")
        j += 1

    j = 1
    while j < i*2:
        print(j, end=" ") # replace j with i
        j += 1

    print()
    i += 1