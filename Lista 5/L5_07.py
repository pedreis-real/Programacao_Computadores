print("\nSUBSTITUIÇÃO DE REPETIÇÕES")
print("A CADA OPERAÇÃO, TECLE 'ENTER'")
texto = input("\nDigite uma frase: ")
novo_texto = ""
count = 0
for i in range(1, len(texto)):
    if texto[i] == texto[i - 1] and count < 1:
        novo_texto += texto[i].upper()
        count += 1
    elif texto[i] != texto[i - 1]:
        if count >= 1:
            count = 0
        else:
            novo_texto += texto[i - 1]
            count = 0
        if i == len(texto) - 1:
            novo_texto += texto[i]
print("\n", novo_texto)
