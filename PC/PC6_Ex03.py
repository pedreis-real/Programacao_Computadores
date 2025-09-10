print("\nVERIFICAÇÃO DE PALÍNDROMO")
print("A CADA OPERAÇÃO, TECLE 'ENTER'")


def verifica(palindromo):
    junta = palindromo.replace(" ", "")
    for i in range(0, len(junta)):
        if junta[i] != junta[len(junta) - 1 - i]:
            return False


frase = input("\nDigite uma frase: ")
if not verifica(frase):
    print("\nÉ palíndromo!")
else:
    print("\nNão é palíndromo!")
