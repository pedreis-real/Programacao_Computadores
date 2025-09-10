with open('arq04.txt', 'r', encoding='utf-8') as entrada:
    dados = entrada.readlines()
    n_pontos = len(dados)
    f = []
    x = []
    y = []
    for i in range(n_pontos):
        linha = dados[i].split(';')
        for j in range(len(linha)):
            linha[j] = float(linha[j].strip())
        # print(linha)
        f += [linha[0]]
        x += [linha[1]]
        y += [linha[2]]
    # print('\nf:', f, '\nx:', x, '\ny:', y, '\n')
