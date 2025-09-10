# num = a + bi
# parte real: a
# parte complexa: bi
# norma: sqrt(a² + b²)
# argumento: arctg((b/a)/norma)
import math
angulos_notaveis = {'π/6': '1/sqrt(3)', 'π/4': '1', 'π/3': 'sqrt(3)',
                    '5π/6': '- 1/sqrt(3)', '3π/4': '- 1', '2π/3': '- sqrt(3)'}


def sep_real_im(num):
    if " " in num:
        num = num.replace(" ", "")
    i = 0
    p = len(num)
    while i < p - 1:
        if i != 0:
            if num[i] == "-":
                if num[i - 1] != "+":
                    antes_menos = num[:i]
                    depois_menos = num[i:]
                    eq = antes_menos + "+" + depois_menos
                    num = eq
                    p += 1
        i += 1
    lis_eq = num.split("+")
    re = lis_eq[0]
    im = lis_eq[1]
    return re, im


def norma_2(z):
    a, b = sep_real_im(z)
    coef_re = int(a)
    coef_im = int(b[:b.find('i')])
    return coef_re**2 + coef_im**2


def arg(z):
    a, b = sep_real_im(z)
    re = int(a)
    im = int(b[:len(b) - 1])
    tan_arg = im/(re*math.sqrt(norma_2(z)))
    return math.degrees(math.atan(tan_arg))


def dec_primos(num):
    pass


'''def soma(z1, z2):
    a1, b1 = sep_real_im(z1)
    re1 = int(a1)
    im1 = int(b1[:len(b1) - 1])
    a2, b2 = sep_real_im(z2)
    re2 = int(a2)
    im2 = int(b2[:len(b1) - 1])
    espaco = " "
    sum = str(re1 + re2)
    sum += espaco + str(im1 + im2) + "i"
    return sum'''


print("\nOPERAÇÕES BÁSICAS NÚMEROS COMPLEXOS"
      "A CADA OPERAÇÃO, TECLE 'ENTER'\n\n")
ze = input("Insira um número complexo na forma algébrica: ")
real, imaginario = sep_real_im(ze)
print(f"\nParte real: {real}\n"
      f"Parte imaginária: {imaginario}\n"
      f"Norma: sqrt({norma_2(ze)})\n"
      f"Argumento: {round(arg(ze), 4)}°")
