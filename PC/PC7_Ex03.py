print("\nLISTA DE COMPRAS")
print("A CADA OPERAÇÃO, TECLE 'ENTER'\n")
compra = []
count = 0
print("Digite os produtos a serem comprados, um por vez, ou 'fim' para finalizar a lista")
while True:
    produto = input()
    if produto == "fim":
        break
    compra += [produto]
    count += 1
if count == 0:
    print("\nA lista está vazia :)")
else:
    print("\nSua lista de compras é:")
    for produto in compra:
        print(produto)
