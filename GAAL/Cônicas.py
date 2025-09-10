def cofator(matriz, n, p, q):
    n_menor = n - 1
    submatriz = []
    for a in range(n):
        linha_sub = []
        for b in range(n):
            if a != p and b != q:
                linha_sub += [matriz[a][b]]
        if len(linha_sub) != 0:
            submatriz += [linha_sub]
    cof = (-1)**(p + q)*determinante(submatriz, n_menor)
    return cof


def determinante(array, n):
    if n == 2:
        a11 = array[0][0]
        a12 = array[0][1]
        a21 = array[1][0]
        a22 = array[1][1]
        det = a11*a22 - a21*a12
    else:
        det = 0
        for k in range(len(array[0])):
            det += array[0][k]*cofator(array, n, 0, k)
        n -= 1
    return det


def imprime_matriz(matriz):
    for m in matriz:
        for n in m:
            print(n, "\t\t\t\t", end="")
        print()


def string_to_list(equacao_inf):
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
    return equacao_inf.split("+")


def determina_coeficientes(equacao):
    coeficientes = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}
    for termo in equacao:
        if "x²" in termo or "x2" in termo:
            if termo.find("x") != 0:
                if termo[termo.find("x") - 1] != "-":
                    coeficientes["A"] = float(termo[:termo.find("x")])
                else:
                    coeficientes["A"] = -1
            else:
                coeficientes["A"] = 1
        if "y²" in termo or "y2" in termo:
            if termo.find("y") != 0:
                if termo[termo.find("y") - 1] != "-":
                    coeficientes["B"] = float(termo[:termo.find("y")])
                else:
                    coeficientes["B"] = -1
            else:
                coeficientes["B"] = 1
        if "xy" in termo:
            if termo.find("x") != 0:
                if termo[termo.find("x") - 1] != "-":
                    coeficientes["C"] = float(termo[:termo.find("x")])
                else:
                    coeficientes["C"] = -1
            else:
                coeficientes["C"] = 1
        if "x" in termo:
            xis = termo.find("x")
            if xis == len(termo) - 1:
                if xis != 0:
                    if termo[xis - 1] != "-":
                        coeficientes["D"] = float(termo[:xis])
                    else:
                        coeficientes["D"] = -1
                else:
                    coeficientes["D"] = 1
        if "y" in termo:
            if termo.find("y") == len(termo) - 1 and termo[termo.find("y") - 1] != "x":
                if termo.find("y") != 0:
                    if termo[termo.find("y") - 1] != "-":
                        coeficientes["E"] = float(termo[:termo.find("y")])
                    else:
                        coeficientes["E"] = -1
                else:
                    coeficientes["E"] = 1
        if "=" in termo:
            if "x" not in termo and "y" not in termo:
                coeficientes["F"] = float(termo[:termo.find("=")])
    return coeficientes


def escreve_matriz(coef):
    matriz = [["2A", "C", "D"], ["C", "2B", "E"], ["D", "E", "2F"]]
    matriz[0][0] = 2*coef["A"]
    matriz[0][1] = coef["C"]
    matriz[0][2] = coef["D"]
    matriz[1][0] = coef["C"]
    matriz[1][1] = 2*coef["B"]
    matriz[1][2] = coef["E"]
    matriz[2][0] = coef["D"]
    matriz[2][1] = coef["E"]
    matriz[2][2] = 2*coef["F"]
    return matriz


def var_analysis(array):
    a = array[0][0]/2
    b = array[1][1]/2
    c = array[0][1]
    d = array[0][2]
    e = array[1][2]
    f = array[2][2]
    alfa = determinante(array, 3)
    beta = 4*a*b - c**2
    gama = a + b
    delta = 4*f*(a + b) - (d**2 + e**2)
    return alfa, beta, gama, delta, a


def identifica_conica(alfa, beta, gama, delta, a):
    if alfa == 0:
        if beta == 0:
            if delta == 0:
                print("duas retas coincidentes")
            else:
                if delta < 0:
                    print("duas retas paralelas distintas")
                else:
                    print("um conjunto vazio em |R²")
        else:
            if beta < 0:
                print("duas retas concorrentes")
            else:
                print("um único ponto")
    else:
        if beta == 0:
            print("uma parábola")
        else:
            if beta < 0:
                print("uma hipérbole")
            else:
                if alfa*gama > 0:
                    print("um conjunto vazio em |R²")
                else:
                    if gama == 2*a:
                        print("uma circunferência")
                    else:
                        print("uma elipse")


print("\nRECONHECIMENTO DE CÔNICAS A PARTIR DO MÉTODO ANALÍTICO")
print("A CADA OPERAÇÃO, TECLE 'ENTER'\n")
print("(lembrando que números decimais são escritos com .)\n")
equacao_informada = input("Insira abaixo a equação de segundo grau nas variáveis x e y na forma"
                          " Ax² + By² + Cxy + Dx + Ey + F = 0\n")
equacao_info = equacao_informada.strip().lower()
if " " in equacao_informada:
    equacao_info = equacao_info.replace(" ", "")
lis_equacao = string_to_list(equacao_info)
dic_coefic = determina_coeficientes(lis_equacao)
matriz_coefic = escreve_matriz(dic_coefic)
_alfa_, _beta_, _gama_, _delta_, _a_ = var_analysis(matriz_coefic)
print(f"\nA equação {equacao_informada} representa ", end="")
identifica_conica(_alfa_, _beta_, _gama_, _delta_, _a_)
