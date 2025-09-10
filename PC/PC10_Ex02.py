def somatorio(n):
    if n == 0:
        soma = 0
    else:
        soma = n + somatorio(n - 1)
    return soma


print("\nSOMA DOS N PRIMEIROS NÚMEROS NATURAIS POR RECURSIVIDADE")
print("A CADA OPERAÇÃO, TECLE 'ENTER'\n")
num = int(input("Insira um número natural diferente de zero: "))
while num <= 0:
    num = int(input("Valor inválido! Insira um número válido: "))
print("\nA soma dos {} primeiros números naturais é {}".format(num + 1, somatorio(num)))
