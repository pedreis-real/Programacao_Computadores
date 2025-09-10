with open("Pares.txt", "r") as pares, open("Múltiplos de 4.txt", "w", encoding="UTF-8") as mult_4:
    mult_4.write("Os 250 primeiros números naturais múltiplos de quatro são:\n")
    for num in pares:
        if len(num) <= 4:
            if int(num) % 4 == 0:
                mult_4.write("{}".format(num))
        else:
            continue
