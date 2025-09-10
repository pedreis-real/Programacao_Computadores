print("CÁLCULO DA ÁREA DE UM CÍRCULO INFORMANDO-SE O RAIO")
print("A CADA OPERAÇÃO TECLE 'ENTER'")
print("(lembrando que números decimais são escritos com .)")
r = float(input("Qual o raio do círculo? "))
while r <= 0:
    print("Isso não é um círculo ")
    r = float(input("Informe um valor válido para o raio "))
A = 3.1415*r**2
print("A área do círculo é de ", A, "u.a.")
