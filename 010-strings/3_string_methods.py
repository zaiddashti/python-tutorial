strSample = "This is a sample String"
print(strSample)

# convert to upper case
print(strSample.upper())


# convert to lower case
print(strSample.lower())


# make it as title
print(strSample.title())


# Removing whitespaces
strSample2 = " This is a sample String with white spaces at the beginning and and the end! "
print(strSample2)           # prints " This is a sample String with white spaces at the beginning and and the end! "
print(strSample2.strip())   # prints "This is a sample String with white spaces at the beginning and and the end!"
print(strSample2.lstrip())  # prints "This is a sample String with white spaces at the beginning and and the end! "
print(strSample2.rstrip())  # prints " This is a sample String with white spaces at the beginning and and the end!"


# Replace string
print(strSample2.replace("beginning", "start"))


# Split string
print(strSample2.split(" ")) # prints ['', 'This', 'is', 'a', 'sample', 'String', 'with', 'white', 'spaces', 'at', 'the', 'beginning', 'and', 'and', 'the', 'end!', '']


# Casecading methods
print(strSample2.strip().split(" ")) # prints ['', 'This', 'is', 'a', 'sample', 'String', 'with', 'white', 'spaces', 'at', 'the', 'beginning', 'and', 'and', 'the', 'end!', '']

