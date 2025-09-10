def string_to_list(equacao_inf):
    equacao_inf = equacao_inf.lower()
    if " " in equacao_inf:
        equacao_inf = equacao_inf.replace(" ", "")
    i = 0
    p = len(equacao_inf)
    while i < p - 1:
        if i != 0:
            if equacao_inf[i] == "-":
                if equacao_inf[i - 1] != "+":
                    antes_menos = equacao_inf[:i]
                    depois_menos = equacao_inf[i:]
                    eq = antes_menos + "+" + depois_menos
                    equacao_inf = eq
                    p += 1
        i += 1
    lis_eq = equacao_inf.split("+")
    print(f"lis_eq: {lis_eq}\n")
    return lis_eq


def list_to_dic(equation):
    dic_valores = {}
    for termo in equation:
        coeficiente = coef(termo)
        for i in range(len(termo)):
            if termo[i].isalpha():
                var = termo[i:]
                print(var)
                if var not in dic_valores.keys():
                    dic_valores[var] = coeficiente
                else:
                    dic_valores[var] += coeficiente
                break
    print(f"dic_valores: {dic_valores}\n")
    return dic_valores


def coef(termo):
    if termo[0].isalpha():
        return 1
    else:
        for i in range(len(termo)):
            if termo[i].isalpha():
                if termo[0] == "-":
                    if termo[1].isnumeric():
                        return int(termo[:i])
                    else:
                        return -1
                else:
                    return int(termo[:i])


def ad_sub(equacao_inf):
    eq_inf = string_to_list(equacao_inf)
    equa = list_to_dic(eq_inf)
    for letra in equa:
        quant = equa[letra]
        if quant > 0:
            if quant == 1:
                quant = " + "
            else:
                quant = " + " + str(quant)
        else:
            if quant == 0:
                quant = str(quant)
            else:
                if quant == -1:
                    quant = " - "
                else:
                    val = str(quant)
                    quant = " - " + val[1:]
        equa[letra] = quant
    print(f"equa: {equa}\n")
    return escreve_new_eq(equa)


def escreve_new_eq(equa):
    new_eq = ""
    for letra, quant in equa.items():
        if quant != "0":
            new_eq += quant + letra
    if new_eq != "":
        new_eq = new_eq.lstrip()
        if new_eq[0] == "+":
            new_eq = new_eq[2:]
        return new_eq
    return 0


print("\nADIÇÃO E SUBTRAÇÃO DE VARIÁVEIS"
      "A CADA OPERAÇÃO, TECLE 'ENTER'\n"
      "(lembrando que números decimais são escritos com .)\n")
equacao = input("Informe uma equacao contendo somas e subtrações de variáveis:\n")
nova_eq = ad_sub(equacao)
print("A equação reduzida é:", nova_eq)
