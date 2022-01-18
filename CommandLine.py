import sys

anzahl = len(sys.argv)
liste = sys.argv

print("Anzahl der Argumente: " + str(anzahl))

x = 0
y = 0

if anzahl >= 3:
    x = int(liste[1])
    y = int(liste[2])
elif anzahl == 2:
    x = int(liste[1])
    y = int(input("Geben Sie die 2. Zahl ein: "))
else:
    x = int(input("Geben Sie die 1. Zahl ein: "))
    y = int(input("Geben Sie die 2. Zahl ein: "))

z = x
z += y
print("\nAddition:                        {0}+={1} =>{2}".format("{0:08b}".format(x), "{0:08b}".format(y),
                                                                 "{0:08b}".format(z)))
print("Addition:                        {0}+={1} =>{2}\n".format(x, y, z))
z = x
z &= y
print("Bitwise AND on operands:         {0}&={1} =>{2}".format("{0:08b}".format(x), "{0:08b}".format(y),
                                                               "{0:08b}".format(z)))
print("Bitwise AND on operands:         {0}&={1} =>{2}\n".format(x, y, z))
z = x
z |= y
print("Bitwise OR on operands:          {0}|={1} =>{2}".format("{0:08b}".format(x), "{0:08b}".format(y),
                                                               "{0:08b}".format(z)))
print("Bitwise OR on operands:          {0}|={1} =>{2}\n".format(x, y, z))
z = x
z ^= y
hi = z
print("Bitwise xOR on operands:         {0}^={1} =>{2}".format("{0:08b}".format(x), "{0:08b}".format(y),
                                                               "{0:08b}".format(z)))
print("Bitwise xOR on operands:         {0}^={1} =>{2}\n".format(x, y, z))
z = x
z >>= y
print("Bitwise right shift on operands: {0}>>={1} =>{2}".format("{0:08b}".format(x), "{0:08b}".format(y),
                                                                "{0:08b}".format(z)))
print("Bitwise right shift on operands: {0}>>={1} =>{2}\n".format(x, y, z))
z = x
z <<= y
print("Bitwise left shift on operands:  {0}<<={1} =>{2}".format("{0:08b}".format(x), "{0:08b}".format(y),
                                                                "{0:08b}".format(z)))
print("Bitwise left shift on operands:  {0}<<={1} =>{2}\n".format(x, y, z))
