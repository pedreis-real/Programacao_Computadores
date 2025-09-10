print("CÁLCULO DO FATORIAL DE UM NÚMERO")
print("A CADA OPERAÇÃO TECLE 'ENTER'")
print(" ")
n = int(input("Informe o número natural desejado: "))
while n < 0:
    n = int(input("O número informado não é natural. Informe um número válido: "))
i = n - 1
f = n
while i > 0:
    f = f * i
    i -= 1
print(" ")
if n == 0:
    print("0! = 1")
else:
    print(n, "! = ", f)
