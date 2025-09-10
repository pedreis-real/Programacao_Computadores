print("PESQUISA")
print("A CADA OPERAÇÃO, TECLE 'ENTER'")
print("(lembrando que números decimais são escritos com .)\n")
print("Informe o sexo (1 para masculino e 2 para feminino) e a altura de 50 pessoas, em sequência")
H = 0
F = 0
Hmin = 100000000000
for i in range(0, 50):
    s = int(input())
    while s != 1 and s != 2:
        s = float(input("Inválido\n"))
    h = float(input())
    if s == 2:
        H = H + h
        F += 1
    if h < Hmin:
        Hmin = h
print("A altura mínima é", Hmin)
if F == 0:
    Med = 0
else:
    Med = H/F
    print("A média da altura das mulheres é", Med)
