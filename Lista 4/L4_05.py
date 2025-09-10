print("\nCÁLULO DO TOTAL EM PARCELA")
print("A CADA OPERAÇÃO, TECLE 'ENTER'")
print("(lembrando que números decimais são escritos com .)\n")


def calcula_pagamento(valor, atraso):
    multa = (3 + 0.1*atraso)*valor/100
    if atraso > 0:
        valor += round(multa, 2)
    print("Multa: R$", multa, sep="")
    return valor


Total = 0
count = 0
while True:
    parcela = float(input("Entre com o valor da parcela em R$ ou digite 0 para sair: "))
    while parcela < 0:
        parcela = int(input("Valor inválido!\n"))
    if parcela == 0:
        break
    dias = int(input("Entre com a quantidae de dias em atraso: "))
    while dias <= 0:
        dias = int(input("Quantidade inválida!\n"))
    Valor = calcula_pagamento(parcela, dias)
    print("O valor a ser pago é R$", Valor)
    Total += Valor
    count += 1
print("\nRelatório do dia:\nParcelas pagas: ", count, "\nValor total das parcelas pagas: R$", Total, sep="")
