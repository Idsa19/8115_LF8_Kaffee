num = 1
eingabe = int(input("Bis zu welchem Wert sollen Primzahlen ausgebenen werden? "))

while num < eingabe:
    primtest = True
    if num != 1 & num != 2 & num != 3:
        i = 2
        while i < num:
            if num % i == 0:
                primtest = False
                break
            i += 1
    if primtest:
        print(num)
    num += 1
