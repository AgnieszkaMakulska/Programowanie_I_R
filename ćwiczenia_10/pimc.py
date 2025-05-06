import numpy as np
import sys

def IntMonteCarlo(f, a, b, N):
    """
    Oblicza przybliżoną wartość całki oznaczonej metodą Monte Carlo.
    (https://en.wikipedia.org/wiki/Monte_Carlo_integration)

    Parametry:
    f - funkcja, którą całkujemy
    a - początek przedziału całkowania
    b - koniec przedziału całkowania
    N - liczba losowych punktów
    """

    # Generowanie N losowych punktów w przedziale [a, b]
    random_points = np.random.uniform(a, b, N)
    
    # Obliczanie wartości funkcji w tych punktach
    function_values = f(random_points)
    
    # Przybliżona wartość całki
    integral = (b - a) * np.sum(function_values) / N
    
    return integral

def f(x):
    return np.sqrt(1 - x**2)

a = -1
b = 1
N = int(sys.argv[1]) if len(sys.argv) > 1 else 100000

# Liczymy przybliżoną wartość liczby pi 100 razy
pi_values = np.array([])
for i in range(100):
    pi_values = np.append(pi_values, 2 * IntMonteCarlo(f, a, b, N))

# Liczymy średnią i odchylenie standardowe
mean = np.mean(pi_values)
variance = np.var(pi_values)

print("Średnia wartość:", mean)
print("Wariancja:", variance)