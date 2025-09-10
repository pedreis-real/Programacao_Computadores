print("CAIXA REGISTRADORA")
print("A CADA OPERAÇÃO, TECLE 'ENTER'")
print("(lembrando que números decimais são escritos com .)\n")
print("Observe a seguinte tabela:\nCódigo\tPreço (R$)\n")
print("1\t0.50\n2\t1.00\n3\t4.00\n5\t7.00\n9\t8.50\n")
s1 = 0
s2 = 0
s3 = 0
s5 = 0
s9 = 0
print("Digite os códigos dos seus produtos em sequência. Digite 0 quando terminar: \n")
while True:
    Cod = int(input())
    while Cod != 0 and Cod != 1 and Cod != 2 and Cod != 3 and Cod != 5 and Cod != 9:
        Cod = int(input("Código inválido! Digite um código válido:\n"))
    if Cod == 0:
        break
    if Cod == 1:
        s1 += 1
    if Cod == 2:
        s2 += 1
    if Cod == 3:
        s3 += 1
    if Cod == 5:
        s5 += 1
    if Cod == 9:
        s9 += 1
p = s1*0.5 + s2 + s3*4 + s5*7 + s9*8.5
print("Você deverá pagar", p, "pelos produtos")
