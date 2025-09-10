print("\nINDICA POSIÇÃO NA LISTA")
print("A CADA OPERAÇÃO, TECLE 'ENTER'")
print("(lembrando que números decimais são escritos com .)\n")


def position(lis, num):
    q = len(lis) - 1
    for i in range(q):
        if lis[i] == num:
            return i
    return -1


count = 0
lista = []
print("Informe um número de cada vez ou '0' para sair: ")
while True:
    n = float(input())
    if n == 0:
        break
    lista.append(n)
    count += 1
pesquisa = float(input("Qual o número a ser encontrado na lista? "))
if count == 0:
    print("A lista está vazia")
else:
    x = position(lista, pesquisa)
    if x == -1:
        print("O número informado não se encontra na lista")
    else:
        print("A primeira aparição do número", pesquisa, "deu-se na posição", x, "da lista")
