from fractions import Fraction


def potenciacao(x, y):
    if y < 0:
        y = - y
    if y == 0:
        return 1
    else:
        if x == 1:
            return 1
        else:
            # x^y = x*x^(y-1)
            return x*potenciacao(x, y - 1)


print("\nPOTENCIAÇÃO DE NÚMEROS INTEIROS POSITIVOS POR RECURSIVIDADE")
print("A CADA OPERAÇÃO, TECLE 'ENTER'\n")
base = int(input("Insira o valor da base: "))
while base < 0:
    base = int(input("Valor inválido! Somente números positivos"))
expoente = int(input("Informe o expoente: "))
if expoente >= 0:
    print(f"\n{base}^{expoente} = {potenciacao(base, expoente)}")
else:
    print(f"\n{base}^{expoente} = {Fraction(1, potenciacao(base, expoente))}")
