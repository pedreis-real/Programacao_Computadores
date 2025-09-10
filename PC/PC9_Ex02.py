with open("Pares.txt", "w", encoding="UTF-8") as pares, open("Ímpares.txt", "w", encoding="UTF-8") as impares:
    pares.write("Os 500 primeiros números naturais pares são:\n")
    impares.write("Os 500 primeiros números naturais ímpares são:\n")
    for i in range(1000):
        if i % 2 == 0:
            pares.write("{}\n".format(i))
        else:
            impares.write("{}\n".format(i))
