import numpy as np
import matplotlib.pyplot as plt
import sys

alpha = 2  # współczynnik dyfuzji cieplnej
dx = 1     # krok przestrzenny
dt = dx**2 / (4 * alpha)  # krok czasowy
l = 50 * dx  # rozmiar płytki
nx = int(l / dx)
ny = int(l / dx)
Nt = 1000  # liczba kroków czasowych

T0 = float(sys.argv[1])
T1 = float(sys.argv[2])
T2 = float(sys.argv[3])
T3 = float(sys.argv[4])
T4 = float(sys.argv[5])

T = np.ones((nx, ny)) * T0 # temperatura początkowa

# Warunki brzegowe
T[0, :] = T1
T[-1, :] = T3
T[:, 0] = T4 
T[:, -1] = T2

for it in range(Nt):

    T_new = T.copy()

    for i in range(1, nx - 1):
        for j in range(1, ny - 1):
            T_new[i, j] = T[i, j] + alpha * dt / dx**2 * (
                T[i+1, j] + T[i-1, j] + T[i, j+1] + T[i, j-1] - 4*T[i, j]
            )

    T = T_new

    if it % 100 == 0:  # zapisuje co 100 kroków
        plt.imshow(T)
        plt.savefig('animation/t='+str(it*dt)+'.png')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('t = {:.2f} s'.format(it * dt))

