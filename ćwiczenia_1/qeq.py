import math
import cmath #funkcje matematyczne liczb zespolonych 

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

delta = b**2 - 4*a*c

if delta == 0:
    x0 = -b / (2*a)
    print("x0 = {0:.2f}".format(x0))
elif delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print("x1 = {0:.2f}\n   x2 = {1:.2f}".format(x1, x2))
else:
    x1 = (-b + cmath.sqrt(delta)) / (2*a)
    x2 = (-b - cmath.sqrt(delta)) / (2*a)
    print("x1 = {0:.2f}\n x2 = {1:.2f}".format(x1, x2))