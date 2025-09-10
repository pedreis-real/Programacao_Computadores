print("\nCONJUGA VERBO TERMINADOS EM 'AR' OU 'ER' NO PRESENTE DO INDICATIVO")
print("A CADA OPERAÇÃO, TECLE 'ENTER'")


def repet(verb):
    p = 0
    while p < len(verb) - 1:
        final = verb[len(verb) - 2] + verb[len(verb) - 1]
        p = verb.find(final, p)
        if p != -1:
            p += 1
    return p - 1


def conjuga(verbo):
    x = repet(verbo)
    term = verbo[x]
    p_sing = list(verbo)
    p_sing[x] = "o"
    p_sing[x + 1] = ""
    um_s = "".join(p_sing)
    s_sing = list(verbo)
    s_sing[x] = term + "s"
    s_sing[x + 1] = ""
    dois_s = "".join(s_sing)
    t_sing = list(verbo)
    t_sing[x] = term
    t_sing[x + 1] = ""
    tres_s = "".join(t_sing)
    p_plural = list(verbo)
    p_plural[x] = term + "mos"
    p_plural[x + 1] = ""
    um_p = "".join(p_plural)
    s_plural = list(verbo)
    s_plural[x] = term + "is"
    s_plural[x + 1] = ""
    dois_p = "".join(s_plural)
    t_plural = list(verbo)
    t_plural[x] = term + "m"
    t_plural[x + 1] = ""
    tres_p = "".join(t_plural)
    print("\nEu", um_s, "\nTu", dois_s, "\nEle/ela", tres_s, "\nNós", um_p, "\nVós", dois_p, "\nEles/elas", tres_p)


ver = input("\nDigite um verbo para que o programe o conjugue: ")
conjuga(ver)
