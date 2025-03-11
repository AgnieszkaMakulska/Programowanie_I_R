k = int(input('Podaj liczbę naturalną k: '))

c = [k]
n = 1

while c[-1] != 1: # przerywamy pętlę while kiedy ostatnim elementem jest 1
    if c[-1] % 2 == 0:
        c.append(int(0.5 * c[-1]))
    elif c[-1] % 2 != 0:
        c.append(int(3 * c[-1] + 1))
    n += 1

print(c)




