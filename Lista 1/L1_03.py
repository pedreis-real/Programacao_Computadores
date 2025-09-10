from math import ceil
print("CUSTO COM TINTA PARA SE PINTAR UM CILINDRO COM RAIO E ALTURA (EM METROS) INFORMADOS PELO USUÁRIO")
print("A CADA OPERAÇÃO TECLE 'ENTER'")
print("(lembrando que números decimais são escritos com .)")
r = float(input("Qual o raio? "))
while r <= 0:
    print("Isso não é um círculo ")
    r = float(input("Informe um valor válido para o raio "))
h = float(input("Qual a altura do cilindro? "))
while h <= 0:
    h = float(input("Informe um valor válido para a altura "))
Ab = 3.1415*r**2
Al = 2*3.1415*r*h
At = 2*Ab + Al
n = ceil(At/15)
C = 50*n
print("Serão necessárias", n, "lata(s) de tinta ao custo de R$", C)
