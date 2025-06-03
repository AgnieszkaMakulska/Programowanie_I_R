import numpy as np
import sys

def IntRectangular(f, a, b, N):

    h = (b - a) / N  # szerokość każdego przdziału
    integral_sum = 0

    for k in range(1, N+1): # k = 1, ..., N
        x_left = a + (k-1) * h #lewy koniec przedziału
        x_right = a + k * h # prawy koniec przedziału  
        midpoint = (x_left + x_right) / 2  # środek przedziału
        integral_sum += h * f(midpoint)

    return integral_sum

def IntTrapezoidal(f, a, b, N):

    h = (b - a) / N  # szerokość każdego przdziału
    integral_sum = 0

    for k in range(1, N+1):
        x_left = a + (k-1) * h #lewy koniec przedziału
        x_right = a + k * h # prawy koniec przedziału  

        integral_sum += h * (f(x_left) + f(x_right)) / 2

    return integral_sum

def IntSimpson(f, a, b, N):

    h = (b - a) / N  # szerokość każdego przdziału
    integral_sum = 0

    for k in range(1, N//2 + 1):
        x_2k_minus_2 = a + (2*k - 2) * h
        x_2k_minus_1 = a + (2*k - 1) * h
        x_2k = a + (2*k) * h 

        integral_sum += (h / 3) * (f(x_2k_minus_2) + 4 * f(x_2k_minus_1) + f(x_2k))

    return integral_sum


def f(t):
    return 1 / t

method = sys.argv[1]
x = float(sys.argv[2])
N = int(sys.argv[3])

if method == "rectangular":
    numerical_integral = IntRectangular(f, 1, x, N)
elif method == "trapezoidal":
    numerical_integral = IntTrapezoidal(f, 1, x, N)
elif method == "simpson":
    numerical_integral = IntSimpson(f, 1, x, N)
else:
    print("Błąd: Nieznana metoda całkowania.")

library_result = np.log(x)

difference = abs(numerical_integral - library_result)

print(f"Całka oznaczona metodą {method}: {numerical_integral}")
print(f"Logarytm naturalny z biblioteki numpy: {library_result}")
print(f"Moduł różnicy: {difference}")