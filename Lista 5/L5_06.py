print("\nCRIA LOGIN")
print("A CADA OPERAÇÃO, TECLE 'ENTER'")


def login(nome):
    nome = nome.strip().lower()
    start = nome[0]
    split = nome.split()
    count = 0
    for i in range(len(nome)):
        if nome[i].isspace():
            count += 1
            if nome[i + 1].isspace():
                count -= 1
    end = split[count]
    string = start + end
    return string


name = input("\nDigite o seu nome: ")
print("Seu login é:", login(name))
