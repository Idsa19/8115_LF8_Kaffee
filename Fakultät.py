def iterativ(num):
    erg = 1
    for x in range(2, (num+1)):
        erg *= x
    return erg


def rekursive(num):
    if num > 1:
        return (num * rekursive(num - 1))
    return 1


print(iterativ(4))
print(rekursive(4))
