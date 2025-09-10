print("TESTE DE DIVISIBILIDADE DE UM NÚMERO INTEIRO POR 2, 3 E 5 AO MESMO TEMPO")
print("A CADA OPERAÇÃO TECLE 'ENTER'")
print("(lembrando que números decimais são escritos com .)")
n = int(input("Em qual número você está pensando? "))
if n % 30 == 0:
    print("O número ", n, "é divisível por 2, 3 e 5 simultaneamente")
else:
    print(n, "não é divisível por 2, 3 e 5 simultaneamente")
    if n % 2 == 0 and n % 3 != 0 and n % 5 != 0:
        print("Em verdade, ", n, "é  divisível somente por 2")
    if n % 2 != 0 and n % 3 == 0 and n % 5 != 0:
        print("Em verdade, ", n, "é  divisível somente por 3")
    if n % 2 != 0 and n % 3 != 0 and n % 5 == 0:
        print("Em verdade, ", n, "é  divisível somente por 5")
    if n % 2 != 0 and n % 3 == 0 and n % 5 == 0:
        print("Em verdade, ", n, "é  divisível somente por 3 e 5")
    if n % 2 == 0 and n % 3 != 0 and n % 5 == 0:
        print("Em verdade, ", n, "é  divisível somente por 2 e 5")
    if n % 2 != 0 and n % 3 != 0 and n % 5 == 0:
        print("Em verdade, ", n, "é  divisível somente por 2 e 3")
    if n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
        print("Em verdade, ", n, "não é divisível por nenhum dos três números")
