from sympy import hermite, legendre, Poly, Symbol

def HermiteCoefficients(n):
    x = Symbol ('x') # tworzy symboliczną zmienną x
    coeffs =  Poly(hermite(n,x),x).all_coeffs() #generuje wielomian i zwraca jego współczynniki, zaczynając od najwyższego stopnia
    return [float(coeff) for coeff in reversed(coeffs)] #odwraca kolejność współczynników i zamienia je na float

def LegendreCoefficients(n):
    x = Symbol ('x')
    coeffs =  Poly(legendre(n, x), x).all_coeffs()
    return [float(coeff) for coeff in reversed(coeffs)]