print("\nCLASSIFICAÇÃO DOS 10 PRIMEIROS COLOCADOS NO BRASILEIRÃO")
print("A CADA OPERAÇÃO, TECLE 'ENTER'")
times = ("Internacional", "Atlético-MG", "São Paulo", "Vasco da Gama",
         "Flamengo", "Palmeiras", "Santos", "Fluminense", "Ceará SC", "Fortaleza")
count = 0
while True:
    if count > 0:
        sim_nao = input("\nContinuar? S/N: ")
        sim_nao = sim_nao.lower()
        while sim_nao != 's' and sim_nao != 'n':
            sim_nao = input("Inválido! Digite 'S' para 'sim' ou 'N' para 'não': ")
        if sim_nao == 'n':
            break
    opcao = int(input("\nOpções do programa"
                      "\n1)Colocação dos n primeiros colocados"
                      "\n2)Mostra a colocação do time informado"
                      "\n3)Lista os n colocados em ordem alfabética inversa"
                      "\nEm todos os casos, n é um número entre 1 e 10, inclusive\n\n"
                      "Digite a opção desejada: "))
    while opcao < 1 or opcao > 3:
        opcao = int(input("Opção inválida! Digite uma opção existente: "))
    if opcao == 1:
        colocados = int(input("\nInforme qual o top a ser mostrado (ex.: digite '10' para top 10): "))
        while colocados < 1 or colocados > 10:
            colocados = int(input("Quantidade inválida! Digite um top válido: "))
        if colocados == 1:
            print("\nO primeiro colocado no Brasileirão foi:")
        else:
            print("\nOs", colocados, "primeiros colocados no Brasileirão foram:")
        for i in range(colocados):
            print(times[i])
    if opcao == 2:
        time_pesq = input("\nInforme o time a ser psequisado: ")
        while time_pesq not in times:
            time_pesq = input("Time não consta entre os dez primeiros colocados."
                              " Digite um time válido. ")
        posicao = times.index(time_pesq) + 1
        print("\nO time ", time_pesq, " está na ", posicao, "° posição do Brasileirão.")
    if opcao == 3:
        print("\nA ordem alfabética inversa é: ")
        ordem_inv_times = sorted(times, reverse=True)
        for clube in ordem_inv_times:
            print(clube)
    count += 1
