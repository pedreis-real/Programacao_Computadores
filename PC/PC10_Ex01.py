def fatorial(n):
    if n != 0:
        fat = n*fatorial(n - 1)
    else:
        fat = 1
    return fat


print("\nCÁLCULO DO FATORIAL DE UM NÚMERO POR RECURSIVIDADE")
print("A CADA OPERAÇÃO, TECLE 'ENTER'\n")
num = int(input("Insira um número natural: "))
while num < 0:
    num = int(input("Valor inválido! Insira um número válido: "))
print("\n{}! = {}".format(num, fatorial(num)))
