def ler_matriz():
    linha = int(input("Informe o número de linhas da matriz: "))
    while linha <= 0:
        linha = int(input("Valor inválido!\n"))
    coluna = int(input("Informe o número de colunas da matriz: "))
    while coluna <= 0:
        coluna = int(input("Valor inválido!\n"))
    print("Insira as entradas da matriz, linha por linha, cada elemento da linha por vez:")
    column = []
    for i in range(linha):
        line = []
        for j in range(coluna):
            entrada = int(input())
            line += [entrada]
        print()
        column += [line]
    return column


def imprime_matriz(matrix):
    for linha in matrix:
        for coluna in linha:
            print(coluna, end="\t\t\t\t\t")
        print("\n")


def escalonamento(array):
    if len(array) == 1:
        return array
    else:
        n_linha = len(array)
        for m in range(n_linha):
            ind = m
            n_coluna = len(array[m])
            pivo = array[m][m]
            while pivo == 0:
                ind += 1
                if ind != n_linha - 1:
                    pivo = array[ind][ind]
                else:
                    break
            if pivo == 0:
                break
            for n in range(n_linha):
                if n != ind:
                    ratio = array[n][ind]/pivo
                    for k in range(n_coluna):
                        array[n][k] -= round(ratio*array[ind][k], 2)
                    imprime_matriz(array)
                    print("\n")
    imprime_matriz(array)


matriz = ler_matriz()
print("\nA matriz digitada é:")
imprime_matriz(matriz)
print("O escalonamento é:")
escalonamento(matriz)
