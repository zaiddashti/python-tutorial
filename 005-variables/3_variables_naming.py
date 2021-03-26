'''
Variable name rules:
1) consists of letters, numbers, and underscores
2) can start with letter or underscore, but not with number
3) spaces are not allowed, but underscore can be used to separate the words
4) avoid using python keywords (reserved words). For example: "for", "if", "not", "while", ...
5) should be short and descriptive
6) becareful when using lowercase "l" and uppercase "O" since they might make some confusion with numbers 1 and 0
'''

# Examples of variable naming
somevar = 10
some_var = 20
_some_var = 30
someVar = 40
SOMEVAR = 50
somevar123 = 60

print(somevar)
print(some_var)
print(_some_var)
print(someVar)
print(SOMEVAR)
print(somevar123)


# incorrect variable naming
# 123some_var       # it starts with number
# some-var          # contains invalid character "-"
# some var          # contains a space