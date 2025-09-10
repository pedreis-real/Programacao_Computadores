s = "um tigre, dois tigres, três tigres"
p = 0
while p < len(s):
    p = s.find("tigre", p)
    if p != -1:
        print("Posição:", p)
        p += 1
