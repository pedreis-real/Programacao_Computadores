import sys
d = int((input("Digite o dia: ")))
m = int(input("Digite o mês: "))
a = int(input("Digite o ano: "))
if a <= 0 or a > 2020:
    print("Data inválida")
else:
    if m <= 0 or m > 12:
        print("Data inválida")
    else:
        if m == 2:
            if a % 4 != 0:
                if d <= 0 or d > 28:
                    print("Data inválida")
                else:
                    print("Data válida")
            else:
                if a % 100 == 0:
                    if a % 400 == 0:
                        if d <= 0 or d > 29:
                            print("Data inválida")
                        else:
                            print("Data válida")
                    else:
                        if d <= 0 or d > 28:
                            print("Data inválida")
                        else:
                            print("Data válida")
                else:
                    if d <= 0 or d > 29:
                        print("Data inválida")
                        sys.exit()
                    else:
                        print("Data válida")
                        sys.exit()
        if m == 4 or m == 6 or m == 9 or m == 11:
            if d <= 0 or d > 30:
                print("Data inválida")
            else:
                print("Data válida")
        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
            if d <= 0 or d > 31:
                print("Data inválida")
            else:
                print("Data válida")
