print("PREÇO DA CONTA DE LUZ")
print("A CADA OPERAÇÃO TECLE 'ENTER'")
print("(lembrando que números decimais são escritos com .)")
print(" ")
c = float(input("Qual foi o consumo de energia elétrica em kWh? "))
while c < 0:
    c = float(input("CONSUMO! Digite corretamente desta vez: "))
print("Qual o tipo de instalação?")
i = int(input("Digite '1' para residências, '2' para comércios e '3' para indústrias: "))
while i <= 0 or i >= 4:
    i = int(input("Instalação inexistente. Digite corretamente o tipo de instalação: "))
if i == 1:
    if c <= 500:
        p = 0.4 * c
        print("Você pagará R$", p, "pelo consumo de energia elétrica.")
    else:
        p = 0.65 * c
        print("Você pagará R$", p, "pelo consumo de energia elétrica.")
if i == 2:
    if c <= 1000:
        p = 0.55 * c
        print("Você pagará R$", p, "pelo consumo de energia elétrica.")
    else:
        p = 0.6 * c
        print("Você pagará R$", p, "pelo consumo de energia elétrica.")
if i == 3:
    if c <= 5000:
        p = 0.55 * c
        print("Você pagará R$", p, "pelo consumo de energia elétrica.")
    else:
        p = 0.6 * c
        print("Você pagará R$", p, "pelo consumo de energia elétrica.")
