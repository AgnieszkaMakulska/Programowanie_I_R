import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.integrate import solve_ivp

# Przykład wywołania: python3 duffing.py 30 0.01

# Parametry oscylatora Duffinga
alpha = 1.0
omega = 1.0
beta = -1.0
delta = 0.2
gamma = 0.3

initial_conditions = [
    [0.99, 0.0],  # x01, v01
    [1.0, 0.0],   # x02, v02
    [1.01, 0.0]   # x03, v03
]

def duffing_oscillator(t, y): # y to stan układu (y=[x, v])
    x,v = y
    dx_dt = v
    dv_dt = -delta * v - alpha * x**3 - beta * x + gamma * np.cos(omega * t)
    return [dx_dt, dv_dt]


# Pobieranie argumentów
tmax = float(sys.argv[1])
dt = float(sys.argv[2])

'''
Rozwiązujemy równania dla każdego zestawu warunków początkowych.
Funkcja scipy.integrate.solve_ivp przyjmuje argmenty:
- funkcję opisującą układ równań różniczkowych
- przedział czasowy
- warunki początkowe
'''
for x0, v0 in initial_conditions:
    sol = solve_ivp(duffing_oscillator, [0, tmax], [x0, v0]) 
    plt.plot(sol.y[0], sol.y[1], label=f"x0={x0}, v0={v0}")
    print(sol.y[0])

# Rysowanie wykresu
plt.xlabel("x")
plt.ylabel("v")
plt.legend()
plt.show()