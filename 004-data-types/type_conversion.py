x = 10          # int
y = 10.5        # float
z = x + y       # float = int + float => implicit casting
print(z)        # 20.5
print(type(x))
print(type(y))
print(type(z))



# Errors:

#newZ = z + "123"    # gives errors, it won't implicit cast it 
#print(newZ)


#var1 = "result = "
#result = var1 + z   # gives errors, it won't implicit cast it
#print(z)