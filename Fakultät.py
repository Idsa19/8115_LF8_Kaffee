def iterativ(num):
    erg = 1
    for x in range(2, (num+1)):
        erg *= x
    return erg


def rekursive(num):
    if num > 1:
        return (num * rekursive(num - 1))
    return 1


n = int(input("Zahl größer 0 eingeben: "))
print(iterativ(n))
print(rekursive(n))

