def iterativ(num):
    erg = 1
    for x in range(2, (num+1)):
        erg *= x
    return erg


def rekursive(num):
    if num > 1:
        return (num * rekursive(num - 1))
    return 1


while True:
    n = int(input("Zahl eingeben: "))
    if n <= 0: break
    print(iterativ(n))
    print(rekursive(n))

