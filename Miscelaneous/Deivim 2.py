def medias(buy):
    dic_media = {}
    for coisa in buy:
        soma = sum(buy[coisa])
        media = soma/len(buy[coisa])
        dic_media[coisa] = media
    print("\nA média de preços por produto foi: ")
    for item, price in dic_media.items():
        print(item, ": ", price, sep="")


def quantidade(dicio):
    dic_quant = {}
    for marcas in dicio:
        quant = len(dicio[marcas])
        dic_quant[marcas] = quant
    print("\nMARCA\t\t\t\t\t\tQUANTIDADE")
    for compras, trem in dic_quant.items():
        print(compras, "\t\t\t\t\t\t", trem)


compra = []
real = []
L_pro = []
D_produto = {}
count = 0
print("\nDigite o nome, a marca (somente uma palavra) e o preço dos produtos comprados"
      ", um por vez, ou 'fim' para finalizar a lista: ")
while True:
    produto = input()
    if produto == "fim":
        break
    product = produto.strip().split()
    n = len(product) - 1
    marca = product[n - 1]
    preco = float(product[n])
    real = [preco]
    if marca not in D_produto:
        D_produto[marca] = real
    else:
        D_produto[marca] += real
    count += 1
if count == 0:
    print("\nA lista está vazia :)")
else:
    opcao = int(input("Expressar em:\n1) Quantidade de produtos da marca\n2) Média de preço por marca\n"))
    while opcao != 1 and opcao != 2:
        opcao = int(input("Opção inválida!\n"))
    if opcao == 1:
        quantidade(D_produto)
    else:
        medias(D_produto)
