print("\nCONTAGEM DE PALAVRAS. ESCREVA UM TEXTO DANDO SOMENTE UM ESPAÇO ENTRE CADA PALAVRA")
print("A CADA OPERAÇÃO, TECLE 'ENTER'\n")
frase = input("Digite uma frase: ")
_frase_ = frase.strip()
count = 0
for i in range(len(_frase_)):
    if _frase_[i].isspace():
        count += 1
        if _frase_[i + 1].isspace():
            count -= 1
print("\nA frase digitada possui", count + 1, "palavra(s).")
