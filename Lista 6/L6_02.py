print("\nCÁLCULO DE NOTA DA TURMA NUMA PROVA DE MÚLTIPLA ESCOLHA")
print("A CADA OPERAÇÃO, TECLE 'ENTER'\n")
alunos = int(input("Quantos alunos há na turma? "))
while alunos <= 0:
    alunos = int(input("Valor inválido!\n"))
n_questoes = int(input("A prova contém quantas questões? "))
while n_questoes <= 0:
    n_questoes = int(input("Valor inválido!\n"))
L_gab = []
print("Digite a alternativa correta de cada questão em sequência e em caixa alta: ")
alternativas = "ABCDE"
for i in range(n_questoes):
    gabarito = input()
    while gabarito not in alternativas:
        gabarito = input("Valor inválido!\n")
    L_gab += [gabarito]
L_matri = []
L_nota = []
for i in range(alunos):
    print("Informe a matrícula do aluno", ": ", sep="", end="")
    matricula = input()
    L_matri += [matricula]
    nota = 0
    print("Informe a alternativa escolhida por este aluno em cada questão, uma por vez:")
    for j in range(n_questoes):
        alt = input()
        if alt == L_gab[j]:
            nota += 1
    L_nota += [nota]
n_aprov = 3*n_questoes/4
count = 0
for k in range(len(L_nota)):
    if L_nota[k] >= n_aprov:
        count += 1
x = 100*round(count/alunos, 2)
print("\nPorcentagem de aprovação: ", x, "%", sep="")
media = round(sum(L_nota)/alunos, 2)
print("A média da turma foi de", media, "pontos")
if sum(L_nota) == L_nota[0]*alunos:
    print("\nNão houveram alunos com nota acima da média. Em verdadem todas as notas foram iguais")
else:
    print("\nOs alunos que obtiveram nota acima da média foram: ")
    for y in range(alunos):
        if L_nota[y] > n_aprov:
            print("Aluno", L_matri[y], "-", "Nota", L_nota[y])
