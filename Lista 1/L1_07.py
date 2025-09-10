print("CLASSIFICAÇÃO DE ACORDO COM O PESO E ALTURA DO USUÁRIO")
print("A CADA OPERAÇÃO TECLE 'ENTER'")
print("(lembrando que números decimais são escritos com .)")
print("Observe a seguinte tabela: ")
print("                                   Peso (em kg)")
print(" Altura(em m)      Menor que 60    Entre 60 e 90    Acima de 90")
print("Menor que 1.20           A               D                G")
print("De 1.20 a 1.70           B               E                H")
print("Maior que 1.70           C               F                I")
print(" ")
print("Classificaremos você de acordo com ela.")
h = float(input("Prinmeiro, diga sua altura: "))
while h <= 0:
    print("Inexistente '-'")
    h = float(input("Qual sua altura real? "))
if h > 2.74:
    print("Você é mais alto que o homem mais alto da história!!!")
m = float(input("Agora informe o se peso: "))
while m <= 0:
    print("Antimatter '-'")
    m = float(input("Informe seu peso real: "))
if m > 597:
    print("Você é mais pesado que o homem mais pesado do mundo!!!")
print(" ")
print("NICE")
print(" ")
if h < 1.2:
    if m < 60:
        print("Você se clasifica na categoria A!")
    if 60 <= m < 90:
        print("Você se clasifica na categoria D!")
    if m > 90:
        print("Você se clasifica na categoria G!")
if 1.2 <= h < 1.7:
    if m < 60:
        print("Você se clasifica na categoria B!")
    if 60 <= m < 90:
        print("Você se clasifica na categoria E!")
    if m > 90:
        print("Você se clasifica na categoria H!")
if h > 1.7:
    if m < 60:
        print("Você se clasifica na categoria C!")
    if 60 <= m < 90:
        print("Você se clasifica na categoria F!")
    if m > 90:
        print("Você se clasifica na categoria I!")
