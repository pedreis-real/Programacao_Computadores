import math
print("\nOPERAÇÕES DIVERSAS. O PROGRAMA FAZ ARREDONDAMENTOS E CONVERSÕES PARA OS INTEIROS SE NECESSÁRIO")
print("A CADA OPERAÇÃO, TECLE 'ENTER'")
print("(lembrando que números decimais são escritos com .)\n")
n = float(input("Entre com um número decimal: ", ))


def fatorial(num):
    fat = 1
    a = round(num)
    if a < 0:
        a = - a
    for i in range(1, a + 1):
        fat *= i
    return fat


def calculo(numero):
    print("Número com apenas uma casa decimal: ", round(numero, 1), sep="")
    int_menor = math.floor(numero)
    int_maior = math.ceil(numero)
    print("Menor inteiro maior ou igual ao número: ", int_maior, sep="")
    print("Maior inteiro menor ou igual ao número: ", int_menor, sep="")
    print("Fatorial do número: ", fatorial(numero), sep="")
    if numero < 0:
        numero = - numero
    print("Raíz quadrada do número: ", math.sqrt(numero), sep="")


calculo(n)
