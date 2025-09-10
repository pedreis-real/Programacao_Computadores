print("\nAGENDA TELEFÔNICA")
print("A CADA OPERAÇÃO, TECLE 'ENTER'\n")
D_agenda = {}
while True:
    L_data_num = []
    opcao = int(input("\nMENU DE OPÇÕES"
                      "\n1)Cadastrar novo contato"
                      "\n2)Consultar um contato"
                      "\n3)Sair"
                      "\n\nInforme uma opção: "))
    while opcao < 1 or opcao > 3:
        opcao = int(input("Opção inválida! Digite uma opção existente: "))
    if opcao == 3:
        break
    if opcao == 1:
        contato = input("\nDigite o dia e o mês de aniversário da pessoa, seu número de telefone e "
                        "seu nome, tudo separado por um espaço simples:\n")
        contato = contato.strip().split()
        nome = ""
        for name in contato[3:]:
            nome += name + " "
        nome = nome.strip()
        data = contato[0] + "/" + contato[1]
        num = contato[2]
        L_data_num.append(data)
        L_data_num.append(num)
        if nome not in D_agenda:
            D_agenda[nome] = L_data_num
        else:
            print("Nome já registrado. Digite um nome ainda não informado após o menu")
    if opcao == 2:
        cont_pesq = input("Informe o contato a ser pesquisado: ")
        while cont_pesq not in D_agenda:
            cont_pesq = input("Nome não consta na agenda! Verifique os dados e insira corretamente: ")
        print("\nData de aniversário:", D_agenda[cont_pesq][0],
              "\nNúmero de telefone:", D_agenda[cont_pesq][1])
