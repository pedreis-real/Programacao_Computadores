print("\nCÁLCULO DE MMC E MDC DE NUMEROS NATURAIS")
print("A CADA OPERAÇÃO, TECLE 'ENTER'\n")


def mdc(numero1, numero2):
    while numero2 != 0:
        resto = numero1 % numero2
        numero1 = numero2
        numero2 = resto
    return numero1


def mmc(numero1, numero2):
    m_m_c = numero1*numero2/mdc(numero1, numero2)
    return m_m_c


while True:
    print("\n1 - Calcular MMC\n2 - Calcular MDC\n3 - Sair")
    cod = int(input("\nDigite a opção: "))
    while cod != 1 and cod != 2 and cod != 3:
        cod = int(input("Código inválido!\n"))
    if cod == 3:
        break
    if cod == 1:
        x = int(input("Digite o primeiro número: "))
        while x < 0:
            x = int(input("Valor inválido!\n"))
        y = int(input("Digite o segundo número: "))
        while y < 0:
            y = int(input("Valor inválido!\n"))
        print("\nO MMC é", mmc(x, y))
    if cod == 2:
        x = int(input("Digite o primeiro número: "))
        while x < 0:
            x = int(input("Valor inválido!\n"))
        y = int(input("Digite o segundo número: "))
        while y < 0:
            y = int(input("Valor inválido!\n"))
        print("\nO MDC é", mdc(x, y))
print("\nVocê saiu do programa!")
