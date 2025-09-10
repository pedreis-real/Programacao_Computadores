def fibonacci(n):
    if n == 1 or n == 2:
        fibo = 1
    else:
        fibo = fibonacci(n - 1) + fibonacci(n - 2)
    return fibo


print("\nCÁLCULO N-ÉSIMO TERMO DA SEQUÊNCIA DE FIBONACCI POR RECURSIVIDADE")
print("A CADA OPERAÇÃO, TECLE 'ENTER'\n")
num = int(input("Qual a posição do termo a ser mostrado? "))
while num <= 0:
    num = int(input("Valor inválido! Insira um número válido: "))
print("\nO {}° termo da sequência de Fibonacci é {}".format(num, fibonacci(num)))
