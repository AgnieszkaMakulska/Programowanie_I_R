import sys
import math
from generator import LCG

N = int(sys.argv[1])

lcg = LCG(x0=10, a=1103515245, b=12345, m=2**31) # generator liczb pseudolosowych

K = 0

for _ in range(N):

    x = lcg() / lcg.max() #dzielimy losowe współrzędne przez lcg.max, żeby były w zakresie [0,1]
    y = lcg() / lcg.max()

    # Sprawdzamy, czy punkt leży w ćwiartce koła o promieniu 1
    if math.sqrt(x**2 + y**2) <= 1:
        K += 1

pi_estimate = 4 * K / N
print(pi_estimate)