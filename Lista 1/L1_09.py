print("\nPÔR TRÊS NÚMEROS DIGITADOS PELO USUÁRIO EM ORDEM DECRESENTE")
print("A CADA OPERAÇÃO TECLE 'ENTER'")
print("(lembrando que números decimais são escritos com .)\n\n")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo: "))
n3 = float(input("Terceiro: "))
print()
if n1 > n2 and n1 > n3:
    if n2 > n3:
        print("A ordem decresente é ", n1, n2, n3)
    else:
        print("A ordem decresente é", n1, n3, n2)
if n2 > n1 and n2 > n3:
    if n1 > n3:
        print("A ordem decresente é ", n2, n1, n3)
    else:
        print("A ordem decresente é", n2, n3, n1)
if n3 > n1 and n3 > n2:
    if n2 > n1:
        print("A ordem decresente é ", n3, n2, n1)
    else:
        print("A ordem decresente é", n3, n1, n2)
