print("DECAIMENTO RADIOATIVO DE UM ELEMENTO COM TEMPO DE MEIA VIDA DE 50s")
print("A CADA OPERAÇÃO, TECLE 'ENTER'")
print("(lembrando que números decimais são escritos com .)\n")
x = float(input("Qual a massa inicial da amostra (em g)? "))
t = 1
m = x
cout = 0
while m >= 0.5:
    m = x*2**(-t/50)
    if t % 50 == 0:
        cout += 1
    print(m)
    t += 1
print("\nPara uma massa de", x, "g, são necessários", t - 1, "segundos para reduzir à menos de 0.5g, sobrando", m,"g dela.")
print("Neste processo, a a mostra passou por", cout, "meias-vidas")

