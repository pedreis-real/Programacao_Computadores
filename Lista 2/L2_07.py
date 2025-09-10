import os
print("MENU DE INTERAÇÃO")
print("A CADA OPERAÇÃO, TECLE 'ENTER'")
print("(lembrando que números decimais são escritos com .)\n")
x = 0
Sal = float(input("Digite o salário: "))
while Sal <= 0:
    Sal = float(input("Valor inválido! Digite um valor válido: "))
while x != 4:
    x = int(input("\nDigite a opção desejada:\n1) Novo Salário\n2) Férias\n3) Décimo terceiro\n4) Sair\n\n"))
    while x <= 0 or x > 4:
        x = int(input("Opção inválida! Digite uma opção válida: "))
    if x == 1:
        if Sal < 1000:
            Sal = Sal*1.15
            print("\nSeu novo salário é de R$", Sal, "\n")
        elif 1000 <= Sal <= 2000:
            Sal = Sal*1.10
            print("\nSeu novo salário é de R$", Sal, "\n")
        elif Sal > 2000:
            Sal = Sal*1.05
            print("\nSeu novo salário é de R$", Sal, "\n")
        os.system("pause")
    if x == 2:
        F = 4*Sal/3
        print("\nO valor de suas férias é de R$ ", F, "\n")
        os.system("pause")
    if x == 3:
        n = int(input("\nQuantos meses você trabalhou na empresa? "))
        while n <= 0 or n > 12:
            n = int(input("Quantidade inválida! Digite uma quantidade válida"))
        S13 = Sal*n/12
        print("\nO valor do seu 13º é de R$", S13, "\n")
        os.system("pause")
print("\nVocê saiu do programa.")
