x = (input("Geben Sie die 1. Zahl ein: "))
y = (input("Geben Sie die 2. Zahl ein: "))

x = float(x)
y = float(y)

z = x+y
print("Addition:        {0} + {1} = {2:.2f}".format(x,y,z))
z = x-y
print("Subtraction:     {0} - {1} = {2:.2f}".format(x,y,z))
z = x*y
print("Multiplikation:  {0} * {1} = {2:.2f}".format(x,y,z))
z = x/y
print("Division:        {0} / {1} = {2:.2f}".format(x,y,z))
z = x%y
print("Rest:            {0} % {1} = {2:.2f}".format(x,y,z))
z = x**y
print("Exponential:     {0} ** {1} = {2:.2f}".format(x,y,z))
z = x//y
print("Floor:           {0} // {1} = {2:.2f}".format(x,y,z))
input()

