print("ÍNDICE PLUVIOMÉTRICO")
print("A CADA OPERAÇÃO, TECLE 'ENTER'")
print("(lembrando que números decimais são escritos com .)\n")
Imax = 0
s = 0
print("Informe o índice pluviométrico de cada dia (em mm), um em cada linha: ")
for i in range(1, 32):
    v = float(input())
    while v < 0:
        v = float(input("Inválido! Digite novamente\n"))
    if v > Imax:
        Imax = v
        dia = i
    s = s + v
print("\nA máxima foi de", Imax, "e ocorreu no dia ", dia, "deste mês")
m = s / i
print("A média pluviométrica no período considerado foi de", m, "mm")
