import math

R = int(input('Podaj promień kuli: '))

if R > 0:
    print('Objętość wynosi ' + str(4/3 * math.pi * R**3))
    print('Pole powiwrzchni wynosi ' + str(4 * math.pi * R**2))
else:
    print("Niepoprawna wartość R")
