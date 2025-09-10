def binario(n):
    digito = n % 2
    if n == 2:
        return "0"
    if n == 1:
        return "1"
    else:
        return binario(int(n/2)) + str(digito)


print("\nTRANSFORMAÇÃO DE UM NÚMERO EM BINÁRIO POR RECURSIVIDADE")
print("A CADA OPERAÇÃO, TECLE 'ENTER'\n")
num = int(input("Informe um número natural: "))
while num <= 0:
    num = int(input("Valor inválido!\n"))
print("{} em binário é {}".format(num, binario(num)))
