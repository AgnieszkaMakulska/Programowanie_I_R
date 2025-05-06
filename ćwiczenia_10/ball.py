import numpy as np
import sys
import matplotlib.pyplot as plt

def BallVolume(n, N):

    # Generujemy N punktów, z których każdy ma n współrzędnych z przedziału [-1,1]
    coordinates = np.random.uniform(-1, 1, size=(N, n))
    
    # Obliczamy kwadraty odległości od środka dla każdego punkty
    distances_squared = np.sum(coordinates**2, axis=1)
    
    # Liczymy ile punktów znajduje się wewnątrz kuli jednostkowej
    n_inside = np.sum(distances_squared <= 1)
    
    # Objętość n-wymiarowego sześcianu
    cube_volume = 2 ** n
    
    # Oszacowanie objętości kuli
    estimated_volume = (n_inside / N) * cube_volume
    return estimated_volume

N = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
k = int(sys.argv[2]) if len(sys.argv) > 2 else 10 # k to maksymalna liczba wymiarów

n_values = np.arange(1, k+1) # n = 1, ..., k

# Obliczamy objętości kuli w wymiarach 1, 2, ..., k
volumes = np.array([BallVolume(n, N) for n in n_values])

# Rysujemy wykres
plt.plot(n_values, volumes, marker='o')
plt.xlabel('n')
plt.ylabel('objętość kuli n-wymiarowej')
plt.show()