print("VERIFICAÇÃO SE UM NÚMERO É PRIMO")
print("A CADA OPERAÇÃO, TECLE 'ENTER'")
print("(lembrando que números decimais são escritos com .)\n")
n = int(input("Qual o número considerado? (naturais somente)\n"))
while n < 0:
    n = int(input("NATURAIS, PORRA! "))
i = 1
count = 0
while i <= n:
    if n % i == 0:
        count += 1
        print(count)
    i += 1
if count == 2:
    print("\n", n, "é primo")
else:
    print("\n", n, "não é primo\nEm verdade,", n, "possui ", count, "divisores")
