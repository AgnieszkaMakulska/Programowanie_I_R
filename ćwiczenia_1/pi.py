import sys

# Żeby uruchomić program np. z n_digits = 3 trzeba wpisać w terminalu:
# python3 lokalizacja_pliku/pi.py 3

def arctg(x):
    result = 0
    Nmax = 100
    for n in range(Nmax):
        result += (-1)**n * x**(2*n + 1)  / (2*n + 1)
    return result

pi = 4 * (4*arctg(1/5) - arctg(1/239))

n_digits = int(sys.argv[1])
print(round(pi,n_digits))