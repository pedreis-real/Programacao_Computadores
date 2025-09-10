print("\nN-ÉSIMO TERMO DA SEQUÊNCIA DE FIBONACCI")
print("A CADA OPERAÇÃO, TECLE 'ENTER'\n")


def fibonacci(n):
    n_menos_1 = 1
    n_menos_2 = 1
    if n == 1:
        return n_menos_2
    elif n == 2:
        return n_menos_1
    else:
        fibo = 0
        for i in range(2, n):
            fibo = n_menos_2 + n_menos_1
            n_menos_2 = n_menos_1
            n_menos_1 = fibo
        return fibo


while True:
    num = int(input("Digite o número do termo a ser calculado: "))
    while num <= 0:
        num = int(input("Valor inválido!\n"))
    print("O ", num, "º termo é ", fibonacci(num), sep="")
    keep = input("Continuar? S/N: ")
    while keep != 'S' and keep != 'N':
        keep = input("Inválido! S/N: ")
    if keep == 'S':
        continue
    if keep == 'N':
        break
