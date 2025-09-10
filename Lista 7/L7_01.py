print("\nNASCIMENTOS POR ANO COM BASE NOS DADOS INFORMADOS")
print("A CADA OPERAÇÃO, TECLE 'ENTER'\n")
L_ano = []
D_ano = {}
print("Digite um ano de nascimento por vez ou '0' para finalizar: ")
while True:
    ano = int(input())
    while ano < 0:
        ano = int(input("Valor inválido! Digite um ano válido: "))
    if ano == 0:
        break
    L_ano += [ano]
for year in L_ano:
    D_ano[year] = D_ano.get(year, 0) + 1
print()
for anos, quant in D_ano.items():
    if quant == 1:
        print("1 pessoa nasceu em", anos)
    else:
        print(quant, "pessoas nasceram em", anos)
