print("\nDETERMINAR SE UM ANO É BISSEXTO")
print("A CADA OPERAÇÃO TECLE 'ENTER'\n\n")
ano = int(input("Informe um ano: "))
if ano < 0:
    ano = -ano
    print("O ano digitado corresponde a ", ano, "a.C.")
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print("O ano digitado é bissexto")
        else:
            print("O ano digitado não é bissexto")
    else:
        print("O ano digitado É bissexto")
else:
    print("O ano não é bissexto")
