def fatorial(n):
    fat = 1
    for i in range(1, n+1):
        fat *= i
    return fat


def porcentagem(x):
    x = str(x)
    zeros = x.count("0")
    if zeros != 0:
        porc = round(100*zeros/len(x), 2)
    else:
        porc = 0
    print("Quantidade de zeros: {}\nQuantidade de números: {}".format(zeros, len(x)))
    return porc


num = int(input())
print("{}! possui {}% de zeros no número".format(num, porcentagem(fatorial(num))))
