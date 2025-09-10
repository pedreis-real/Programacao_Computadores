from time import sleep


def le_prefeitos():
    with open("Prefeitos.txt", "r", encoding='UTF-8') as prefeitos:
        dic_prefeitos = {}
        for linha in prefeitos.readlines():
            prefeito, numero = linha.split(",")
            numero = numero.replace("\n", "")
            dic_prefeitos[numero] = prefeito
    return dic_prefeitos


def le_vereadores():
    with open("Vereadores.txt", "r", encoding="UTF-8") as vereadores:
        dic_vereador = {}
        for linha in vereadores.readlines():
            if ":" in linha:
                partido = linha[:len(linha) - 2]
            else:
                vereador, numero = linha.split(",")
                numero = numero.replace("\n", "")
                dic_vereador[numero] = vereador, partido
    return dic_vereador


def le_partidos():
    with open("Partidos.txt", "r", encoding="UTF-8") as partidos:
        dic_partidos = {}
        for linha in partidos.readlines():
            partido, numero, vagas = linha.split(",")
            vagas = vagas.replace("\n", "")
            dic_partidos[numero] = partido, vagas
    return dic_partidos


def votacao(party, major, verea):
    dic_votos_ver = {}
    dic_votos_pref = {}
    dic_votos_partidos = {}
    while True:
        num_ver = input("VEREADOR: ")
        num_ver = num_ver.lower()
        if num_ver == "poderes de adm":
            print("VOTAÇÕES ENCERRADAS!")
            break
        if num_ver not in verea.keys():
            if len(num_ver) == 2:
                if num_ver in party.keys():
                    dic_votos_partidos[num_ver] = dic_votos_partidos.get(num_ver, 0) + 1
                else:
                    dic_votos_ver["nulo"] = dic_votos_ver.get("nulo", 0) + 1
            else:
                dic_votos_ver["nulo"] = dic_votos_ver.get("nulo", 0) + 1
        else:
            if num_ver == "branco":
                dic_votos_ver["branco"] = dic_votos_ver.get("branco", 0) + 1
            else:
                dic_votos_ver[num_ver] = dic_votos_ver.get(num_ver, 0) + 1
                partido = num_ver[:2]
                dic_votos_partidos[partido] = dic_votos_partidos.get(partido, 0) + 1
        num_pref = input("\nPREFEITO: ")
        num_pref = num_pref.lower()
        if num_pref not in major.keys():
            dic_votos_pref["nulo"] = dic_votos_pref.get("nulo", 0) + 1
        else:
            if num_pref == "branco":
                dic_votos_pref["branco"] = dic_votos_pref.get("branco", 0) + 1
            else:
                dic_votos_pref[num_pref] = dic_votos_pref.get(num_pref, 0) + 1
        print("COMPUTANDO SEU VOTO...")
        sleep(1)
        print("FIM!")
    return dic_votos_partidos, dic_votos_pref, dic_votos_ver


def escreve_eleitos(partido, prefeito, vereador, dados_party):
    with open("Dados votação", "w", encoding="UTF-8") as votos:
        total = 0
        nulos = [0, 0]
        brancos = [0, 0]
        for chave in partido:
            total += partido[chave]
        for chave in prefeito:
            if chave == "nulo":
                nulos[0] += prefeito[chave]
            if chave == "branco":
                brancos[0] += prefeito[chave]
            total += prefeito[chave]
        for chave in vereador:
            if chave == "nulo":
                nulos[1] += vereador[chave]
            if chave == "branco":
                brancos[1] += vereador[chave]
            total += vereador[chave]
        votos.write(f"TOTAL DE VOTOS: {total}\n"
                    f"VOTOS BRANCOS: {sum(brancos)} ({round(sum(brancos)/(100*total), 2)}%)\n"
                    f"    - Prefeito: {brancos[0]} ({round(brancos[0]/(100*total), 2)}%)\n"
                    f"    - Vereador: {brancos[1]} ({round(brancos[1]/(100*total), 2)}%)\n"
                    f"VOTOS NULOS: {sum(nulos)} ({round(sum(nulos)/(100*total), 2)}%)\n"
                    f"    - Prefeito: {nulos[0]} ({round(nulos[0]/(100 * total), 2)}%)\n"
                    f"    - Vereador: {nulos[1]} ({round(nulos[1]/(100 * total), 2)}%)\n")
        pass


part, pref, ver = le_partidos(), le_prefeitos(), le_vereadores()
votos_part, votos_pref, votos_ver = votacao(part, pref, ver)
escreve_eleitos(votos_part, votos_pref, votos_ver, part)
print(f"dic_partidos:\n{part}\n\ndic_prefeitos:\n{pref}\n\ndic_vereadores:\n{ver}\n\n"
      f"votos_part:\n{votos_part}\n\nvotos_pref:{votos_pref}\n\nvotos_ver:\n{votos_ver}")
