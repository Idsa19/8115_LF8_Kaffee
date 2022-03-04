x = 1
print("Gerade Zahlen: ", end='')
while x <= 100:
    if x % 2 == 0:
        print(str(x) + ", ", end='')
    x += 1
x = 1
print("\nUngerade Zahlen: ", end='')
while x <= 100:
    if x % 2 == 1:
        print(str(x) + ", ", end='')
    x += 1
