def ler_matriz():
    ordem = int(input("Informe a ordem da matriz: "))
    while ordem <= 1:
        ordem = int(input("Valor inválido!\n"))
    print("Insira as entradas da matriz, linha por linha, cada elemento da linha por vez:")
    column = []
    for i in range(ordem):
        line = []
        for j in range(ordem):
            entrada = int(input())
            line += [entrada]
        column += [line]
    return column


def imprime_matriz(matriz):
    for m in matriz:
        for n in m:
            print(n, "\t\t", end="")
        print()


def cofator(matriz, n, p, q):
    n_menor = n - 1
    submatriz = []
    for a in range(n):
        linha_sub = []
        for b in range(n):
            if a != p and b != q:
                linha_sub += [matriz[a][b]]
        if len(linha_sub) != 0:
            submatriz += [linha_sub]
    cof = (-1)**(p + q)*determinante(submatriz, n_menor)
    return cof


def determinante(array, n):
    if n == 2:
        a11 = array[0][0]
        a12 = array[0][1]
        a21 = array[1][0]
        a22 = array[1][1]
        det = a11*a22 - a21*a12
    else:
        det = 0
        for k in range(len(array[0])):
            det += array[0][k]*cofator(array, n, 0, k)
        n -= 1
    return det


print("\nCÁLCULO DE DETERMINANTE DE MATRIZES DE ORDEM 2 OU SUPERIOR")
print("A CADA OPERAÇÃO, TECLE 'ENTER'\n")
matrix = ler_matriz()
orden = len(matrix)
determ = determinante(matrix, orden)
print("\nO determinante da matriz")
imprime_matriz(matrix)
print("vale", determ)
