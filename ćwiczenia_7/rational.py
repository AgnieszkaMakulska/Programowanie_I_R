from math import gcd # największy wspólny dzielnik (greatest common divisor)

class RationalNumber:
    def __init__(self, p=0, q=1):
        if q == 0 or p != int(p) or q != int(q): # sprawdzamy czy p i q są całkowite i czy mianownik nie jest 0
            print("Nieprawidłowe argumenty")
        else:
            # dzielimy licznik i mianownik przez największy wspólny dzielnik:
            common_divisor = gcd(p, q)
            self.p = p // common_divisor
            self.q = q // common_divisor

            if self.q < 0: # jeśli mianownik jest ujemny, zmieniamy znak licznika i mianownika (żeby mieć -1/6 zamiast 1/-6)
                self.p = -self.p
                self.q = -self.q

    def numerator(self):
        return self.p
    
    def denominator(self):
        return self.q
    
    def __float__(self): # przeładowanie operatora float
        return float(self.p / self.q)
    
    def __neg__(self): # przeładowanie operatora zmiany znaku -
        return RationalNumber(-self.p, self.q)
    
    def __lt__(self, other): # przeładowanie operatora <
        return self.p / self.q < other.p / other.q # zwraca True albo False
    
    def __add__(self, other): # przeładowanie operatora +
        return RationalNumber(self.p * other.q + self.q * other.p, self.q * other.q)
    
    def __sub__(self, other): # przeładowanie operatora odejmowania -
        return RationalNumber(self.p * other.q - other.p * self.q, self.q * other.q)
    
    def __mul__(self, other): # przeładowanie operatora *
        return RationalNumber(self.p * other.p, self.q * other.q)
    
    def __div__(self, other): # przeładowanie operatora /
        return RationalNumber(self.p * other.q, self.q * other.p)
    
    def __iadd__(self, other): # przeładowanie operatora +=
        self.p = self.p * other.q + self.q * other.p
        self.q = self.q * other.q
        return self
    
    def __isub__(self, other): # przeładowanie operatora -=
        self.p = self.p * other.q - other.p * self.q
        self.q = self.q * other.q
        return self
    
    def __imul__(self, other): # przeładowanie operatora *=
        self.p = self.p * other.p
        self.q = self.q * other.q
        return self
    
    def __idiv__(self, other): # przeładowanie operatora /=
        self.p = self.p * other.q
        self.q = self.q * other.p
        return self
    
    def __repr__(self): # reprezentacja obiektu jako str
        return f"RationalNumber(p={self.p}, q={self.q})"
    
    def __str__(self): # uproszczona reprezentacja obiektu jako str
        return f"{self.p}/{self.q}"



p1, q1 = [int(x) for x in input("Podaj pierwszą liczbę: ").split('/')]
p2, q2 = [int(x) for x in input("Podaj drugą liczbę: ").split('/')]

r1 = RationalNumber(p1, q1)
r2 = RationalNumber(p2, q2)

print(f"Liczby w postaci dziesiętnej: {float(r1)}, {float(r2)}")
print(f"Liczby przeciwne do podanych: {-r1}, {-r2}")

if not r2 < r1:
    print(f"Liczby w kolejności niemalejącej: {r1}, {r2}")
else:
    print(f"Liczby w kolejności niemalejącej: {r2}, {r1}")

print(f"Suma: {r1 + r2}")
print(f"Iloczyn: {r1 * r2}")
