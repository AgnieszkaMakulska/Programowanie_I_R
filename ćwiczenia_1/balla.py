import sys
import math

# Żeby uruchomić program np. z R = 5 trzeba wpisać w terminalu
# python3 lokalizacja_pliku/balla.py 5

R = int(sys.argv[1])
if R > 0:
    print(f"Pole powierzchni: {4 * math.pi * R**2:.2f}") #formatowanie z dokładnością do 2 miejsc po przecinku
    print(f"Objętość: {(4/3) * math.pi * R**3:.2f}")
else:
    print("Niepoprawna wartość R")