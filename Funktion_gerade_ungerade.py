def gerade (n):
    if (n%2) == 0:
        return True
    return False


print("Die Zahlen von 1 - 100: ")
for x in range(1, 101, 1):
    print(str(x), str(gerade(x)) + ", ")
