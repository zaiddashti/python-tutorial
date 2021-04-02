# Some examples in this lesson such as
# lists, tuples, dictionaries, functions, classes
# are advanced to this video topic and will be explained in the later videos
# Booleans values are either True or False

# Example 1
print(True)         # True
print(False)        # False


print("==========")

# Example 2
print(100 > 5.75)   # True
print(100 < 5.75)   # False
print(100 == 100)   # True
print(100 == 5.75)  # False


print("==========")

# Example 3
x = 100
y = 5.75
if x > y:
    print("Expression x > y is evaluated to True")
else:
    print("Expression x > y is evaluated to False")


print("==========")

# Example 4
print(bool("Some String"))  # True
print(bool(5.75))           # True  (any number is True except 0)
print(bool(-5.75))           # True  (any number is True except 0)
print(bool(0))              # False (0 is always False)


print("==========")

# Example 5
someString = "Some String"
y = 5.75
yNeg = -5.75
ZERO = 0
print(bool(someString))  # True
print(bool(y))           # True  (any number is True except 0)
print(bool(yNeg))        # True  (any number is True except 0)
print(bool(ZERO))        # False (0 is always False)


# Most values are true except
# 1) 0
# 2) empty string
# 3) empty list, tuple, and dictionary

print("==========")

# Example 6 on True
print(bool("Not empty string"))
print(bool(100))
print(bool(["car", "plane", "boat"]))


print("==========")

# Example 7 on False
print(bool(False))
print(bool(None))
print(bool(""))
print(bool(0))
print(bool([]))
print(bool(()))
print(bool({}))


print("==========")

# Example 8 on functions returning boolean values
def someFunction():
    return True

print(someFunction())


print("==========")

# Example 9 on functions used in if-statement
if someFunction():
  print("Statements when True")
else:
  print("Statements when False")



print("==========")

# Example 10 on classes (return False when method __len__() returns 0)
class someClass():
  def __len__(self):
    return 0

someObj = someClass()
print(bool(someObj))


print("==========")

# Example 11 isinstance
print(isinstance(x, int))
print(isinstance(y, float))
print(isinstance(someString, str))
print(isinstance(someObj, someClass))