print("SOMA DOS N PRIMEIROS TERMOS DA SEQUÊNCIA an = (-1/n)^(n+1)")
print("A CADA OPERAÇÃO, TECLE 'ENTER'")
print("(lembrando que números decimais são escritos com .)\n")
n = int(input("Digite a quantidade de termos desejada: "))
while n <= 0:
    n = int(input("Inválido! Digite novamente: "))
s = 0
for i in range(1, n + 1):
    num = (-1)**(i+1)
    s = s + num/i
print("\nA soma dos", n, "termos da sequência vale ", s)
