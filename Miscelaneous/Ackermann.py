import sys
sys.setrecursionlimit(100000000)


def ack(m, n):
    if m == 0:
        return n + 1
    else:
        if n == 0:
            return ack(m - 1, 1)
        else:
            return ack(m - 1, ack(m, n - 1))


with open("Ackermann's function.txt", "w", encoding="utf-8") as ackermann:
    for i in range(5):
        if i != 4:
            for j in range(9):
                ackermann.write(f"ack({i}, {j}) = {ack(i, j)}\n")
        else:
            for j in range(1):
                ackermann.write(f"ack({i}, {j}) = {ack(i, j)}\n")
