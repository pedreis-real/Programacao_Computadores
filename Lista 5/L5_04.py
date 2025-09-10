print("\nTROCA VOGAIS POR *")
print("A CADA OPERAÇÃO, TECLE 'ENTER'")
frase = input("\nDigite uma frase: ")
vogais = "aáàãâAÁàÃÂeéêEÉÊiíIÍoóõôOÓÕÔuúUÚ"
for i in range(len(vogais)):
    if vogais[i] in frase:
        frase = frase.replace(vogais[i], "*")
print(frase)
