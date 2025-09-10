print("SOMA DOS NÚMEROS PARES CONTIDOS NO INTERVALO INFORMADO PELO USUÁRIO")
print("A CADA OPERAÇÃO TECLE 'ENTER'")
print("(lembrando que números decimais são escritos com .)")
print(" ")
Inf = int(input("Informe o limitante inferior do intervalo: "))
Sup = int(input("Agora informe o limitante superior: "))
while Sup <= Inf:
    Sup = int(input("Limitante inválido por não determinar um intervalo condizente. Informe um número válido: "))
i = Inf
cont = 0
s = 0
while i < Sup:
    if i % 2 == 0:
        cont += 1
        s = s + i
    i += 1
print("Existem", cont, "números pares no intervalo")
print("A soma é", s)
