print("CÁLCULO DO SEU IMC")
print("A CADA OPERAÇÃO TECLE 'ENTER'")
print("(lembrando que números decimais são escritos com .)")
print("O Índice de Massa Corporal (IMC) de uma pessoa é a razão de sua massa e altura")
m = float(input("Quanto você pesa, em kg? "))
while m <= 0:
    print("Antimatter '-'")
    m = float(input("Informe seu peso real: "))
if m > 597:
    print("Você é mais pesado que o homem mais pesado do mundo!!!")
print("NICE")
h = float(input("Agora informe sua altura: "))
while h <= 0:
    print("Inexistente '-'")
    h = float(input("Qual sua real altura? "))
if h > 2.74:
    print("Você é mais alto que o homem mais alto da história!!!")
imc = m/h**2
print("Seu IMC é de ", imc, ". Obrigado por participar do programa :)")
