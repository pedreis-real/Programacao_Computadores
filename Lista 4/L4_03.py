print("\nVERIFICAÇÃO DE QUADRADO PERFEITO")
print("A CADA OPERAÇÃO, TECLE 'ENTER'\n")


def quad_perf(num):
    raiz = int(num ** (1 / 2))
    if raiz ** 2 == num:
        return True
    else:
        return False


n = int(input("Entre com um número: "))
while n < 0:
    n = int(input("Valor inválido!\n"))
if quad_perf(n):
    print(n, "é quadrado perfeito!")
else:
    print(n, "não é quadrado perfeito!")
