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
    for x in range(n + 1):
        sum += x
    return sum


def Sum4(n):
    if n > 0:
        return (n + Sum4(n - 1))
    return 0

num = 997

print(Sum1(num))
print(Sum2(num))
print(Sum3(num))
print(Sum4(num))
