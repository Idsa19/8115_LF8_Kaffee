x = int(input("Geben Sie die 1. Zahl ein: "))
y = int(input("Geben Sie die 2. Zahl ein: "))

z = x
z += y
print("Addition: {0}+={1} =>{2}".format(x, y, z))
z = x
z &= y
print("Bitwise AND on operands:         {0}&={1} =>{2}".format(x, y, z))
z = x
z |= y
print("Bitwise OR on operands:          {0}|={1} =>{2}".format(x, y, z))
z = x
z ^= y
print("Bitwise xOR on operands:         {0}^={1} =>{2}".format(x, y, z))
z = x
z >>= y
print("Bitwise right shift on operands: {0}>>={1} =>{2}".format(x, y, z))
z = x
z <<= y
print("Bitwise left shift on operands:  {0}<<={1} =>{2}".format(x, y, z))
