from PolynomialClass import Polynomial #zdefiniowana przez nas klasa
from Coefficients import HermiteCoefficients, LegendreCoefficients # funkcje do liczenia współczynników

class HermitePolynomial(Polynomial):
    def __init__(self, n): # n to stopień wielomianu
        self.n = n
        self.c = HermiteCoefficients(n)

class LegendrePolynomial(Polynomial):
    def __init__(self, n): # n to stopień wielomianu
        self.n = n
        self.c = LegendreCoefficients(n)

n = int(input("Podaj n: "))
x = float(input("Podaj x: "))

Hn = HermitePolynomial(n)
Ln = LegendrePolynomial(n)
print("Hn(x) = ", Hn(x))
print("Ln(x) = ", Ln(x))

Hn_derivative = Hn.D()
Ln_derivative = Ln.D()

result = Hn_derivative(x) + Ln_derivative(x) + 3 * (Hn(x) + Ln(x))
print("H'n(x) + L'n(x) + 3(Hn(x)+Ln(x)) = ", result)
