def leitura():
    dimention_base = int(input("Informe a dimensão da base: "))
    while dimention_base <= 0:
        dimention_base = int(input("Valor inválido!\n"))
    dimention_vetor = int(input("Informe a dimensão do vetor: "))
    while dimention_vetor <= 0:
        dimention_vetor = int(input("Valor inválido!\n"))
    print("Insira as coordenadas de cada vetor, um por vez:")
    base = []
    for i in range(dimention_base):
        vetor = []
        for j in range(dimention_vetor):
            entrada = int(input())
            vetor += [entrada]
        base += [vetor]
    return base


def soma(u, v):
    lis_sum = []
    for i in range(len(u)):
        lis_sum += [round(u[i] + v[i], 4)]
    return lis_sum


def diferenca(u, v):
    lis_dif = []
    for i in range(len(u)):
        lis_dif += [round(u[i] - v[i], 4)]
    return lis_dif


def norma(vetor):
    soma_quadr = 0
    for u in vetor:
        soma_quadr += u**2
    norm = soma_quadr**(1/2)
    return norm


def produto(v1, v2):
    prod = 0
    for i in range(len(v1)):
        prod += v1[i]*v2[i]
    return prod


def projecao(a, b):
    escalar = produto(a, b)/norma(b)**2
    vec_proj = []
    for vetor in b:
        vetor *= escalar
        vec_proj += [vetor]
    return vec_proj


def verifica_ortogonalidade(base):
    for i in range(len(base)):
        u = base[i]
        for j in range(len(base)):
            v = base[j]
            if j != i:
                prod = produto(u, v)
                if prod == 0:
                    return True
                else:
                    return False


def ortogonal(base_info):
    if verifica_ortogonalidade(base_info):
        base_gonal = base_info
    else:
        base_gonal = []
        for k in range(len(base_info)):
            if k == 0:
                w = base_info[k]
                base_gonal += [w]
            else:
                base_proj = []
                for p in range(len(base_gonal)):
                    proj = projecao(base_info[k], base_gonal[p])
                    base_proj += [proj]
                soma_proj = base_proj[0]
                for i in range(len(base_proj)):
                    soma_proj = soma(base_proj[i], soma_proj)
                    if i == len(base_proj) - 1:
                        w = diferenca(base_info[k], soma_proj)
                        base_gonal += [w]
    return base_gonal


def ortonormal(base_w):
    base_normal = []
    for i in range(len(base_w)):
        vec_norm = []
        for j in range(len(base_w[i])):
            coord_norm = round(base_w[i][j]/norma(base_w[i]), 4)
            vec_norm += [coord_norm]
        base_normal += [vec_norm]
    return base_normal


def imprime_base(matrix):
    for linha in matrix:
        for coluna in linha:
            print(coluna, end="\t\t\t\t\t")
        print("\n")


print("\nPROCESSO DE GRAM-SCHMDT")
print("A CADA OPERAÇÃO, TECLE 'ENTER'\n")
base_dada = leitura()
print("\n\nA base informada está apresentada abaixo, de modo que cada vetor corresponde a uma linha da matriz: ")
imprime_base(base_dada)
base_ortogonal = ortogonal(base_dada)
base_ortonormal = ortonormal(base_ortogonal)
print("\nA partir do processo de Gram-Schmidt, o programa obteve:")
imprime_base(base_ortogonal)
print("como base ortogonal a partir da base informada\n\nE:")
imprime_base(base_ortonormal)
print("como base ortonormal")
