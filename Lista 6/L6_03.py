from string import ascii_lowercase


def letras_disponiveis(letras_utilizadas, finder, alfabeto):
    if acerto(finder):
        lis_alf = list(alfabeto)
        for i in range(len(letras_utilizadas)):
            lis_alf.remove(letras_utilizadas[i])
        return lis_alf


def acerto(letrosa):
    if letrosa in palavra:
        return True
    else:
        return False


def simplificador(pesquisa):
    ah = "áàâã"
    for a in range(len(ah)):
        if ah[a] in pesquisa:
            pesquisa = pesquisa.replace(ah[a], "a")
    eh = "éèê"
    for e in range(len(eh)):
        if eh[e] in pesquisa:
            pesquisa = pesquisa.replace(eh[e], "e")
    ih = "íìî"
    for i in range(len(ih)):
        if ih[i] in pesquisa:
            pesquisa = pesquisa.replace(ih[i], "i")
    oh = "óòôõ"
    for o in range(len(oh)):
        if oh[o] in pesquisa:
            pesquisa = pesquisa.replace(oh[o], "o")
    uh = "úùû"
    for u in range(len(uh)):
        if uh[u] in pesquisa:
            pesquisa = pesquisa.replace(uh[u], "u")
    cedilha = "ç"
    if cedilha in pesquisa:
        pesquisa = pesquisa.replace("ç", "c")
    return pesquisa


print("\nJOGO DA FORCA")
print("A CADA OPERAÇÃO, TECLE 'ENTER'\n")
print("Escolha o nível do jogo:\n1) Fácil - 15 tentativas\n2) Médio - 10 tentativas\n3) Difícil - 6 tentativas", sep="")
nivel = int(input())
while nivel != 1 and nivel != 2 and nivel != 3:
    nivel = int(input("Valor inválido!\n"))
max_tentativas = 0
if nivel == 1:
    max_tentativas = 15
if nivel == 2:
    max_tentativas = 10
if nivel == 3:
    max_tentativas = 6
p_alavra = input("\nQual a palavra secreta (certifique-se que o jogador não a veja)? ")
palavra = p_alavra.strip().lower()
palavra = simplificador(palavra)
count = 0
for letra in ascii_lowercase:
    if letra in palavra:
        count += 1
n_letras = count
L_util = []
descoberta = palavra
for n in range(len(descoberta)):
    if not descoberta[n].isspace():
        descoberta = descoberta.replace(descoberta[n], "_")
tentativas = 1
tracos = 0
dif = n_letras - tentativas
n_tracos = descoberta.count("-")
L_alf = ascii_lowercase
print("\n\n\n\n\n\n")
while dif >= 0:
    print(descoberta, sep="")
    if tentativas != max_tentativas:
        letra_pesq = input("\nDigite uma letra a ser pesquisada na palavra secreta: ")
        if tentativas > 1:
            while letra_pesq in L_util:
                letra_pesq = input("A letra digitada já foi utilizada. Digite uma válida: ")
        letra_pesq = simplificador(letra_pesq)
        L_util += [letra_pesq]
        if acerto(letra_pesq):
            p = 0
            while p < len(palavra):
                p = palavra.find(letra_pesq, p)
                if p != -1:
                    temp = list(descoberta)
                    temp[p] = letra_pesq
                    descoberta = "".join(temp)
                    p += 1
                else:
                    break
            if descoberta == palavra:
                print("\nVOCÊ GANHOU O JOGO :) PARABÉNS!!!")
                break
            print("\n\nLetra constra na palavra secreta!")
            print("\nPalavra até então ", descoberta, sep="")
            print("Letras disponíveis", letras_disponiveis(L_util, letra_pesq, L_alf), "\n")
        else:
            print("\nLetra não consta na palavra secreta!")
            print(letras_disponiveis(L_util, letra_pesq, L_alf))
        if descoberta == palavra:
            print("\nVOCÊ GANHOU O JOGO :) PARABÉNS!!!")
            break
        if n_tracos <= 4:
            advinhar = input("Deseja adivinhar a apalavra? Digite 's' se sim ou 'n' se não: ")
            while advinhar != "s" and advinhar != "n":
                advinhar = input("Inválido! Insira um valor válido: ")
            if advinhar == "s":
                guessu = input("ÚLTIMA TENTATIVA! Adivinhe a palavra: ")
                if guessu == p_alavra or guessu == palavra:
                    print("\nVOCÊ GANHOU O JOGO :) PARABÉNS!!!")
                    break
                else:
                    print("\nGAME OVER!")
                    break
    else:
        guess = input("ÚLTIMA TENTATIVA! Adivinhe a palavra: ")
        if guess == p_alavra or guess == palavra:
            print("\nVOCÊ GANHOU O JOGO :) PARABÉNS!!!")
        else:
            print("\nGAME OVER!")
    L_alf = ascii_lowercase
    tentativas += 1
    dif = n_letras - tentativas
    n_tracos = descoberta.count("-")
