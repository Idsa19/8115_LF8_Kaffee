num = 1
eingabe = int(input("Bis zu welchem Wert sollen Primzahlen ausgebenen werden? "))

while num < eingabe:
    primtest = True
    if num == 1:
        primtest = False
    else:
        i = 2
        while i <= num:
            if num % i == 0:
                primtest = False
            i += 1
            if primtest == True:
                print(num)
    num += 1