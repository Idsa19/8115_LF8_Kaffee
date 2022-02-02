num = 1
eingabe = int(input("Bis zu welchem Wert sollen Primzahlen ausgebenen werden? "))

while num < eingabe:
    primtest = True
    if num % 2 == 0 and num != 2:
        primtest = False;
    elif num != 1 and num != 2 and num != 3:
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                primtest = False
                break
    if primtest:
        print(num)
    num += 1
