print("\nCONTAGEM DE QUANTAS VEZES UM CARACTERE APARECE")
print("A CADA OPERAÇÃO, TECLE 'ENTER'")
frase = input("\nDigite uma frase: ")
frase = frase.upper()
for i in range(len(frase)):
    if i == 0:
        print("")
    char = frase[i]
    if char != "¬":
        p = frase.count(char)
        print(frase[i], ": ", p, sep="")
        frase = frase.replace(char, "¬")
