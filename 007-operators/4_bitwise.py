x = 0b00001100  # 0000 1100 = 12
y = 0b00000101  # 0000 0101 = 5
r = 0b00000000  # 0000 0000 = 0

r = x & y;        # 4 = 0000 1000
print ("The value of r is " + str(r))

r = x | y;        # 13 = 0000 1101 
print ("The value of r is " + str(r))

r = ~x;           # -13 = 1111 0011
print ("The value of r is " + str(r))

r = x ^ y;        # 9 = 0000 1001
print ("The value of r is " + str(r))

r = x << 2;       # 48 = 0011 0000
print ("The value of r is " + str(r))

r = x >> 2;       # 3 = 0000 0011
print ("The value of r is " + str(r))