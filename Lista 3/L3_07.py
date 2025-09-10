print("DIVESORES DOS NÚMEROS DE 2 A 100, UM POR VEZ")
print("A CADA OPERAÇÃO, TECLE 'ENTER'")
print("(lembrando que números decimais são escritos com .)\n")
for i in range(2, 101):
    print(i, ": ", end='\t')
    for j in range(1, i+1):
        if i % j == 0:
            print(j, end='\t')
    print("\n")
