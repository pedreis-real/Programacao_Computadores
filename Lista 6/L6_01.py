print("\nMÉDIA DE TEMPERATURA")
print("A CADA OPERAÇÃO, TECLE 'ENTER'\n")
meses = "Janeiro, Fevereiro, Março, Abril, Maio, Junho, Julho, Agosto, Setembro, Outubro, Novembro, Dezembro"
L_meses = meses.split(",")
medias = []
for mes in L_meses:
    print("Digite a temperatura média do mês de ", mes, ", em °C: ", sep="", end="")
    temperatura = float(input())
    medias += [temperatura]
temp_media = round(sum(medias)/12, 2)
print("\nA média das temperaturas foi de ", temp_media, "°C", sep="")
if sum(medias) == medias[0]*12:
    print("\nNão houveram meses com temperatura acima da média, sendo todas as méidas mensais iguais.")
else:
    print("\nO(s) mes(es) com temperatura acima da média foi(foram): ")
    for i in range(len(L_meses)):
        if medias[i] > temp_media:
            print(L_meses[i], ": ", medias[i], "°C", sep="")
