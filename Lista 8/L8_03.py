def harmonico(n):
    if n == 1:
        harm = 1
    else:
        harm = harmonico(n - 1) + 1/n
    return round(harm, 6)


print("\nRESTO DA DIVISÃO POR RECURSIVIDADE")
print("A CADA OPERAÇÃO, TECLE 'ENTER'\n")
num = int(input("Informe um número natural: "))
while num <= 0:
    num = int(input("Valor inválido!\n"))
print("O harmônico de {} é {}".format(num, harmonico(num)))
