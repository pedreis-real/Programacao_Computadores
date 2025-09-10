print("NÚMEROS ESPELHADOS")
print("A CADA OPERAÇÃO, TECLE 'ENTER'")
print("(lembrando que números decimais são escritos com .)\n")
n = int(input("Digite o número natural (diferente de 0) a ser sequenciado em ordem cresente e decresente: "))
while n < 0:
    n = int(input("NATURAL!!! "))
while n == 0:
    n = int(input("DIFERENTE DE 0 !!! "))
for i in range(1, n+1):
    print("\n", i, "\t\t\t", n+1-i)
