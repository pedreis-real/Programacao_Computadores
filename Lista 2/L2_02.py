print("CÁLCULO DA MÉDIA PLUVIOMÉTRICA EM UM INTERVALO DE 31 DIAS E DETERMINAÇÃO DA MÁXIMA NESTE INTERVALO")
print("A CADA OPERAÇÃO, TECLE 'ENTER'")
print("(lembrando que números decimais são escritos com .)\n")
Imax = 0
i = 1
s = 0
dia = 30
print("Informe o índice pluviométrico de cada dia (em mm), um em cada linha: ")
while i <= 31:
    v = float(input())
    while v < 0:
        v = float(input("Inválido! Digite novamente\n"))
    if v > Imax:
        Imax = v
        dia = i
    s = s + v
    i += 1
print("\nA máxima foi de", Imax, "e ocorreu no dia ", dia, "deste mês")
m = s / 31
print("A média pluviométrica no período considerado foi de", m, "mm")
