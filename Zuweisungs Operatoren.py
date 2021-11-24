x = int(input("Geben Sie die 1. Zahl ein: "))
y = int(input("Geben Sie die 2. Zahl ein: "))

z = x
z += y
print("Addition:                        {0}+={1} =>{2}".format(x, y, z))
z = x
z &= y
print("{0}&={1} =>{2}".format(x, y, z))
z = x
z |= y
print("{0}|={1} =>{2}".format(x, y, z))
z = x
z ^= y
print("{0}^={1} =>{2}".format(x, y, z))
z = x
z >>= y
print("Verschiebe um y bit nach rechts: {0}>>={1} =>{2}".format(x, y, z))
z = x
z <<= y
print("Verschiebe um y bit nach links:  {0}<<={1} =>{2}".format(x, y, z))
