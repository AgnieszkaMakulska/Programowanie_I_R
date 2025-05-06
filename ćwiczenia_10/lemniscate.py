import numpy as np
import sys

def LemniscateArea(N):

    # Całkujemy w obszarze [-1.5, 1.5] x [-0.6, 0.6]
    x_min, x_max = -1.5, 1.5
    y_min, y_max = -0.6, 0.6

    # Generowanie N losowych punktów w obszarze całkowania
    x_random = np.random.uniform(x_min, x_max, N)
    y_random = np.random.uniform(y_min, y_max, N)

    # Sprawdzamy ile punktów jest wewnątrz lemniskaty
    n_inside = 0
    for x, y in zip(x_random, y_random):
        if (x**2 + y**2)**2 <= 2 * (x**2 - y**2):
            n_inside += 1

    # Pole całego obszaru
    area_total = (x_max - x_min) * (y_max - y_min)

    # Przybliżone pole powierzchni lemniskaty
    lemniscate_area = area_total * n_inside / N

    return lemniscate_area


N = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
print("Pole lemniskaty:", LemniscateArea(N))