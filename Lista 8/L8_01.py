def resto(x, y):
    if x > y:
        return resto(x-y, y)
    if x < y:
        return x
    if x == y:
        return 0


print("\nRESTO DA DIVISÃO POR RECURSIVIDADE")
print("A CADA OPERAÇÃO, TECLE 'ENTER'\n")
num1 = int(input("Informe o primeiro número natural: "))
while num1 < 0:
    num1 = int(input("Valor inválido!\n"))
num2 = int(input("Informe o segundo: "))
while num2 < 0:
    num2 = int(input("Valor inválido!\n"))
print("O resto da divisão entre {} e {} é {}".format(num1, num2, resto(num1, num2)))
