def ler_matriz():
    linhas = int(input("Informe o número de linhas da matriz: "))
    while linhas <= 0:
        linhas = int(input("Valor inválido!\n"))
    colunas = int(input("Informe o número de linhas da matriz: "))
    while colunas <= 0:
        colunas = int(input("Valor inválido!\n"))
    print("Insira as entradas, linha por linha, cada elemento da linha por vez:")
    column = []
    for i in range(linhas):
        line = []
        for j in range(colunas):
            entrada = float(input())
            line += [entrada]
        column += [line]
    return column


def imprime_matriz(matriz):
    for m in matriz:
        for n in m:
            print(n, "\t", end="")
        print()


def verificar_matriz(array):
    for p in range(len(array)):
        for q in range(len(array[p])):
            if array[p][q] == array[q][p]:
                continue
            else:
                return False
    return True


print("\nVEIRIFICAÇÃO DE SIMETRIA DE MATRIZES")
print("A CADA OPERAÇÃO, TECLE 'ENTER'\n")
matrix = ler_matriz()
print("\nA matriz informada foi:")
imprime_matriz(matrix)
if verificar_matriz(matrix):
    print("E ela é simétrica")
else:
    print("E ela não é simétrica")
