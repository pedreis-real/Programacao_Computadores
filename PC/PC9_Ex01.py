print("\nTABUADA EM ARQUIVO")
print("A CADA OPERAÇÃO, TECLE 'ENTER'\n")
num = int(input("Digite um número de 0 a 10: "))
while num < 0 or num > 10:
    num = int(input("Valor inválido! Entre com um número válido: "))
arquivo = open("Tabuada.txt", "w")
arquivo.write("Tabuada do {}:\n\n".format(num))
for i in range(0, 11):
    arquivo.write("{} x {}  =  {}\n".format(num, i, num*i))
arquivo.close()
