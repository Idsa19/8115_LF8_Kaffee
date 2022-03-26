def gerade (n):
    if (n % 2):
        return True
    return False


print("Die Zahlen von 1 - 100: ")
for x in range(101):
    print(str(x), str(gerade(x)) + ", ")
