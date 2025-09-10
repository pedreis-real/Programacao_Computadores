print("MAIOR E MENOR ALTURA; MÉDIA DE ALTURA DAS MULHERES")
print("A CADA OPERAÇÃO TECLE 'ENTER'")
print("(lembrando que números decimais são escritos com .)")
print(" ")
i = 0
cont = 0
H = 0
Hmax = 0
h = float(input("Forneça uma altura: "))
while h <= 0:
    h = float(input("Altura inválida. Informe uma válida: "))
Hmin = h
s = int(input("De qual sexo? Digite '1' para 'masculino' e '2' para 'feminino': "))
while s != 1 and s != 2:
    s = int(input("Inexistente. Diga corretamente o sexo: "))
while i < 49:
    h = float(input("Forneça uma altura: "))
    while h <= 0:
        h = float(input("Altura inválida. Informe uma válida: "))
    s = int(input("De qual sexo? Digite '1' para 'masculino' e '2' para 'feminino': "))
    while s != 1 and s != 2:
        s = int(input("Inexistente. Diga corretamente o sexo: "))
    if s == 2:
        cont += 1
        H = H + h
    if h > Hmax:
        Hmax = h
    if h < Hmin:
        Hmin = h
    i += 1
m = H / cont
print(" ")
print("A maior altura registrada é", Hmax, "e a menor é", Hmin)
print("A média de altura das mulheres é", m)
