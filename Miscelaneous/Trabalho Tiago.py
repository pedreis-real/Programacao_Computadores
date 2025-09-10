def le_vetor():
    pass


def valida_entrada():
    pass


def repete_numeros():
    pass


def calcula_fatorial():
    pass


def seq_fibonacci():
    pass


def num_fibonacci():
    pass


def primos_op1():
    print("\nInsira um número por vez ou -1 para parar de inserir números:")
    primos = []
    numeros_totais = []
    while True:
        num = int(input())
        if num == -1:
            break
        while num < -2 or num == 0:
            num = int(input("Valor inválido! Digite um valor válido: "))
        while num in numeros_totais:
            num = int(input("O número já apereceu! Digite outro número: "))
        if num not in numeros_totais:
            numeros_totais += [num]
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count == 2:
            primos += [num]
    primos.sort()
    imprime_primos(primos, 1, num)


def imprime_primos(primos, opcao, n):
    ultimo = primos[len(primos) - 1]
    primos = primos[:len(primos) - 1]
    if opcao == 1:
        print("\nDentre os números digitados, aqueles que são primos são:")
    else:
        print(f"\nOs números primos de 1 a {n}")
    for numero in primos:
        print(numero, end=", ")
    print(ultimo)


def primos_op2():
    num = int(input("Insira um número natural diferente de zero: "))
    primos = []
    for i in range(1, num + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count == 2:
            primos += [i]
    imprime_primos(primos, 2, num)


def fatorial_op3():
    pass


def fatorial_op4():
    pass


def fibonacci_op5():
    pass


def fibonacci_op6():
    pass


def continuar():
    sim_nao = input("\n\nDeseja realizar outra operação? (S/N): ")
    while sim_nao != "S" or sim_nao != "N":
        sim_nao = input("Somente S/N: ")
    return sim_nao


s_n = "s"
while s_n == "s":
    opcao = int(input("\n\t\t\t\t----MENU DE OPÇÕES:----\n\nSelecione a opção desejada:\n"
                      "1 - Retorna todos os números que são primos em uma lista de números que digitar\n"
                      "2 - Retorna todos os números primos de 1 até N\n"
                      "3 - Retorna cada número pertencente a uma lista e o seu fatorial\n"
                      "4 - Retorna o fatorial do número N até 0\n"
                      "5 - Retorna a sequência de fibonacci de 0 até o n-ésimo termo\n"
                      "6 - Retorna todos os números que fazem parte da sequencia de fibonacci\n\n"
                      "Digite a opção desejada: "))
    while opcao < 1 or opcao > 6:
        opcao = input(f"\nO número que você digitou ({opcao}) não pertence ao intervalo permitido.\n"
                      f"Insira um valor válido: ")
    if opcao == 1:
        primos_op1()
    if opcao == 2:
        primos_op2()
    if opcao == 3:
        fatorial_op3()
    if opcao == 4:
        fatorial_op4()
    if opcao == 5:
        fibonacci_op5()
    if opcao == 6:
        fibonacci_op6()
    s_n = continuar()
