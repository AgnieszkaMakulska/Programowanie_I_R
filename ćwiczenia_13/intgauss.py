import sys
import numpy as np
from numpy.polynomial import legendre

'''
Metoda Gaussa-Legendre'a przybliża wartość całki przez sumę ważoną wartości funkcji w określonych punktach (węzłach).
https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_quadrature

Węzły i wagi dla metody Gaussa-Legendre'a są zdefiniowane dla przedziału [-1, 1]. 
Jeśli chcemy obliczyć całkę w przedziale [a, b], musimy przeskalować zmienną 
całkowania (https://en.wikipedia.org/wiki/Gaussian_quadrature#Change_of_interval)
'''

def IntGauss(f, a, b, q, w):
        
    # Transformacja zmiennych z przedziału [-1, 1] do [a, b]
    x = (b - a) / 2 * q + (a + b) / 2

    # Obliczenie sumy ważonej wartości funkcji w węzłach
    integral_sum = np.sum(w * f(x))

    # Przeskalowanie wyniku
    integral = (b - a) / 2 * integral_sum

    return integral

def IntGaussN(f, a, b, n):
    
    q, w = legendre.leggauss(n)
    return IntGauss(f, a, b, q, w)

def f(t):
    return 1 / t

x = float(sys.argv[1])
n = int(sys.argv[2])

if n not in (2, 3, 4, 5):
    print("Błąd: Liczba węzłów musi być równa 2, 3, 4 lub 5.")

else:
    numerical_integral = IntGaussN(f, 1, x, n)

    library_result = np.log(x)

    difference = abs(numerical_integral - library_result)

    print(f"Całka: {numerical_integral}")
    print(f"Logarytm naturalny z biblioteki numpy: {library_result}")
    print(f"Moduł różnicy: {difference}")