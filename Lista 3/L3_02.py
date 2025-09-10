print("PESQUISA POPULACIONAL")
print("A CADA OPERAÇÃO, TECLE 'ENTER'")
print("(lembrando que números decimais são escritos com .)\n")
count = 0
i = 0
while True:
    i = int(input("Informe a idade: "))
    while i < -1 or i == 0:
        i = int(input("Inválida! Insira uma idade válida: "))
    if i == -1:
        break
    s = input("Informe o sexo (m/f): ")
    while s != 'm' and s != 'f' and s != 'M' and s != 'F':
        s = input("Somente 'm' e 'f' são válidos. Digite novamente o sexo: ")
    c = input("Qual a cor dos cabelos? (loiro, castanho, preto ou outro): ")
    while c != 'loiro' and c != 'castanho' and c != 'preto' and c != 'outro':
        c = input("Cor inválida! Digite novamente a cor dos cabelos: ")
    o = input("Irforme a cor dos olhos (azul, verde ou castanho - claro, médio e escuro considerados - ou preto: ")
    while o != 'azul' and o != 'verde' and o != 'castanho' and o != 'preto':
        o = input("Cor inválida! Digite novamente a cor dos olhos: ")
    if 18 <= i <= 35 and s == 'f' and o == 'verde' and c == 'loiro':
        count += 1
print("\nExistem", count, "mulheres com idade entre 18 e 35 anos que possuem cabelo loiro e olho verde no grupo")
