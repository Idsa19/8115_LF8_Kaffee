def Sum1(n):
    return int((n * (n + 1)) / 2)


def Sum2(n):
    sum = 0
    while n > 0:
        sum += n
        n -= 1
    return sum


def Sum3(n):
    sum = 0
    for x in range(1, n + 1):
        sum += x
    return sum


def Sum4(n):
    if n > 0:
        return (n + Sum4(n - 1))
    return 0


print(Sum1(4))
print(Sum2(4))
print(Sum3(4))
print(Sum4(4))
