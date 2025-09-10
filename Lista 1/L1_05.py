print("CONDIÇÕES DE PAGAMENTO DO PEDIDO")
print("A CADA OPERAÇÃO TECLE 'ENTER'")
print("(lembrando que números decimais são escritos com .)")
print("SUas condições de pagamento são:")
print("1 - À vista em dinheiro, recebendo 10% de desconto")
print("2 - Em 1x no cartão de crédito ou cheque, recebendo 5% de desconto")
print("3 - Em 2x no cartão de crédito ou cheque, pagando o valor original do produto no montante")
print("4 - Em 3x no cartão de crédito ou cheque, com 10% de juros no valor final do produto")
p = float(input("Qual o valor do produto? "))
while p <= 0:
    if p < 0:
        print("Você é o comprador, não o vendedor '-'")
        p = float(input("Insira o valor real do produto "))
    if p == 0:
        print("Não trabalhamos com gratuidade")
        p = float(input("Insira o valor real do produto "))
c = int(input("Qual será a forma de pagamento? Coloque de acordo com o código listado acima "))
while c <= 0 or c >= 5:
    c = int(input("Não temos essa forma de pagamento. Insira uma válida "))
if c == 1:
    Pf = 0.9*p
    print("Você pagará R$", Pf, "pelo produto. Obrigado e volte sempre!!")
if c == 2:
    Pf = 0.95 * p
    print("Você pagará R$", Pf, "pelo produto. Obrigado e volte sempre!!")
if c == 3:
    Pf = p
    Par1 = Pf/2
    print("Você pagará duas vezes de R$", Par1, "pelo produto. Obrigado e volte sempre!!")
if c == 4:
    Pf = 1.1*p
    Par2 = Pf/3
    print("Você pagará três vezes de R$", Par2, "pelo produto. Obrigado e volte sempre!!")
