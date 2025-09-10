print("SOMA FINITA DA SEQUÊNCIA an = (2*n - 1)/(n + 1)")
print("A CADA OPERAÇÃO, TECLE 'ENTER'")
print("(lembrando que números decimais são escritos com .)\n")
i = 1
S = 0
n = int(input("Quantos termos devem ser computados (defaut: 50)? "))
while n <= 0:
    n = int(input("Valor invélido! Insira novamente quantos números devem ser computados? "))
while i <= n:
    num = 2*i - 1
    den = i
    S = S + num / den
    i += 1
    print(S)
print("\nA soma dos", n, "termos dessa sequência vale", S)
