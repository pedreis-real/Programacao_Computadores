print("CÁLCULO DE IDADE DE ACORDO COM A DATA INFORMADA PELO USUÁRIO")
print("A CADA OPERAÇÃO TECLE 'ENTER'")
print(" ")
ano_inf = int(input("Qual o ano considerado? "))
mes_inf = int(input("E o mês? "))
while mes_inf <= 0 or mes_inf > 12:
    mes_inf = int(input("Mês inválido. Informe um mês válido: "))
dia_inf = int(input("E o dia? "))
while dia_inf <= 0 or dia_inf > 31:
    dia_inf = int(input("Dia inválido. Informe um dia válido: "))
if ano_inf % 4 != 0 and mes_inf == 2:
    while dia_inf <= 0 or dia_inf >= 29:
        while dia_inf > 31:
            dia_inf = int(input("Dia inválido. Informe um dia válido: "))
        dia_inf = int(input("Fevereiro possuiu somente 28 dias no ano informado. Digite o dia corretamente: "))
if ano_inf % 4 == 0 and mes_inf == 2:
    while dia_inf <= 0 or dia_inf >= 30:
        dia_inf = int(input("Dia inválido. Informe novamente o dia considerado: "))
while mes_inf == 4 or mes_inf == 6 or mes_inf == 9 or mes_inf == 11 and dia_inf == 31:
    dia_inf = int(input("O mês informado só possui 30 dias. Informe novamente o dia do seu nascimento: "))
print(" ")
ano_nasc = int(input("Em que ano você nasceu? "))
while ano_nasc > ano_inf:
    ano_nasc = int(input("Ano inválido. Informe um ano válido: "))
print(" ")
mes_nasc = int(input("Em qual mês? Números apenas "))
while mes_nasc <= 0 or mes_nasc > 12:
    mes_nasc = int(input("Mês inválido. Informe um mês válido: "))
print(" ")
dia_nasc = int(input("Por último, digite o dia em que você nasceu: "))
while dia_nasc <= 0 or dia_nasc > 31:
    dia_nasc = int(input("Dia inválido. Informe um dia válido: "))
if ano_nasc % 4 != 0 and mes_nasc == 2:
    while dia_nasc <= 0 or dia_nasc >= 29:
        while dia_nasc <= 0 or dia_nasc > 31:
            dia_nasc = int(input("Dia inválido. Informe um dia válido: "))
        dia_nasc = int(input("Fevereiro possuiu somente 28 dias no ano informado. Digite novamente o dia do seu nascimento "))
if ano_nasc % 4 == 0 and mes_nasc == 2:
    while dia_nasc <= 0 or dia_nasc >= 30:
        dia_nasc = int(input("Dia inválido. Informe novamente o dia do seu nascimento: "))
if mes_nasc == 4 or mes_nasc == 6 or mes_nasc == 9 or mes_nasc == 11:
    while dia_nasc == 31:
        dia_nasc = int(input("O mês informado só possui 30 dias. Informe novamente o dia do seu nascimento: "))
print(" ")
if ano_nasc < 0:
    ano_nasc = -ano_nasc
    print("Você nasceu no dia ", dia_nasc, "do ", mes_nasc, " de ", ano_nasc, "a.C.")
else:
    print("Você nasceu no dia ", dia_nasc, "do ", mes_nasc, " de ", ano_nasc, ".")
print(" ")
if mes_nasc <= mes_inf and dia_nasc < dia_inf:
    if ano_nasc > 0:
        idade = ano_inf + ano_nasc - 1
        print("Você possui ", idade, "anos.")
    else:
        idade = ano_inf - ano_nasc - 1
        print("Você possui ", idade, "anos.")
else:
    if ano_nasc > 0:
        idade = ano_inf + ano_nasc
        print("Você possui ", idade, "anos.")
    else:
        idade = ano_inf - ano_nasc
        print("Você possui ", idade, "anos.")
