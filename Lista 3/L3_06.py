print("PESQUISA POPULACIONAL - NASCIMENTOS PREMATUROS")
print("A CADA OPERAÇÃO, TECLE 'ENTER'")
print("(lembrando que números decimais são escritos com .)\n")
n = int(input("Quantas crianças nasceram no período considerado? "))
while n <= 0:
    n = int(input("Inválido! Digite corretamente: "))
print("Forneça o sexo da criança prematura (m/f) e, em seguida, o número de dias que ela permaneceu na emcubadora")
M = 0
F = 0
Dia = 0
count = 0
for i in range(n):
    s = input()
    while s != 'M' and s != 'F' and s != 'X':
        s = input("Inválido! Digite 'm' para 'masculino' e 'f' para 'feminino' ")
    if s == 'X':
        break
    if s == 'M':
        M += 1
    if s == 'F':
        F += 1
    d = int(input())
    while d < 0:
        d = input("Invalido! Digite uma quantidade válida: ")
    Dia = Dia + d
    print("F: ", F, "\tM: ", M, "\tTotal de dias na incubadora: ", Dia, "\tQuantidade de recém-nascidos: ", i)
    count += 1
PorcPre = 100 * count / n
PorcPreM = 100 * M / count
PorcPreF = 100 * F / count
Med = Dia / count
print("\n- Porcentagem de recém-nascidos prematuros: ", PorcPre, "%")
print("- Porcentagem de recém-nascidos meninos do total de prematuros:  ", PorcPreM, "%")
print("- Porcentagem de recém-nascidos meninas do total de prematuros: ", PorcPreF, "%")
print("- Média de dias de permanência dos recém-nascidos prematuros na incubadora", Med, "%")
