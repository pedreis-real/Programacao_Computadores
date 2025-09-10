string1 = input("\nInsira o primeiro texto: ")
string2 = input("Insira o segundo texto: ")
count = 0
for i in range(0, len(string2)):
   if string2[i] in string1:
      count += 1
if count == len(string2):
   print("É substring")
else:
   print("Não é substring")
