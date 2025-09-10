print("\nINVERÇÃO DA ENTRADA")
print("A CADA OPERAÇÃO, TECLE 'ENTER'\n")
count = 0
lista = []
print("Informe um número de cada vez ou '0' para sair: ")
while True:
    n = float(input())
    if n == 0:
        break
    lista += [n]
    count += 1
if count == 0:
    print("Você não inseriu nenhum valor")
else:
    q = len(lista) - 1
    print("A ordem inversa de inserção é ", end="")
    for i in range(q, 0, -1):
        print(lista[i], end=", ")
    print(lista[0])
