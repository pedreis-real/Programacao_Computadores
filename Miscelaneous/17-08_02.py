from time import sleep
print("CRONÔMETRO")
print("A CADA OPERAÇÃO, TECLE 'ENTER'")
print("(lembrando que números decimais são escritos com .)\n")
for h in range(0, 24):
    digH = ""
    if h < 10:
        digH = "0"
    for m in range(0, 60):
        digM = ""
        if m < 10:
            digM = "0"
        for s in range(0, 60):
            digS = ""
            if s < 10:
                digS = "0"
            print(digH, h, ": ", digM, m, ":", digS, s, sep="")
            sleep(1)
