def mdc(x, y):
    if y == 0:
        return x
    else:
        return mdc(y, x % y)


print("\nMÁXIMO DIVISOR COMUM POR RECURSIVIDADE")
print("A CADA OPERAÇÃO, TECLE 'ENTER'\n")
num1 = int(input("Informe o primeiro número natural: "))
while num1 < 0:
    num1 = int(input("Valor inválido!\n"))
num2 = int(input("Informe o segundo: "))
while num2 < 0:
    num2 = int(input("Valor inválido!\n"))
print("O máximo divisor comum entre {} e {} é {}".format(num1, num2, mdc(num1, num2)))
