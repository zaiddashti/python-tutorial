# correct, expected to multiply by 2
for x in range(5):
    print(x*2)

print("====================")

# incorrect, expected to multiply by 2, but it is powered of 2
for x in range(5):
    print(x**2) # let's say by mistake you add 1 more "*"
