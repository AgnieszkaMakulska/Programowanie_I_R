import math

class Mean:

    def __init__(self, x): # x to lista liczb
        self.x = x
        
    def N(self):
        return len(self.x)
    
    def __call__(self):
        print("Ta metoda jest zaimplementowana w klasie dziedziczącej")
    '''
    To, że klasa Mean ma posiadać wirtualny bezargumentowy operator wywołania (),
    oznacza, że definiujemy metodę __call__, ale jako metodę abstrakcyjną 
    (czyli taką, która nie jest implementowana w klasie bazowej, 
    a jedynie wymuszamy jej implementację w klasach dziedziczących.
    '''


class ArithmeticMean(Mean): # klasa dziedziczy po klasie Mean
    def __call__(self):
        if not self.x: # 0 jeśli lista jest pusta
            return 0
        else:
            return sum(self.x) / len(self.x)
        

class GeometricMean(Mean): 
    def __call__(self):
        if not self.x:
            return 0
        else:
            product = math.prod(self.x)  # iloczyn elementów listy
            return product ** (1 / len(self.x))
        
class HarmonicMean(Mean):
    def __call__(self):
        if not self.x or any(num == 0 for num in self.x): # 0, jeśli lista jest pusta lub zawiera 0
            return 0
        else:
            return self.N() / sum(1 / num for num in self.x)

    
numbers = [float(x) for x in input("Podaj liczby oddzielone spacjami: ").split()]

#tworzymy obiekty
arithmetic_mean = ArithmeticMean(numbers)
geometric_mean = GeometricMean(numbers)
harmonic_mean = HarmonicMean(numbers)

#wywołujemy metody __call__ każdego z obiektów
print("Średnia arytmetyczna:", arithmetic_mean())
print("Średnia geometryczna:", geometric_mean())
print("Średnia harmoniczna:", harmonic_mean())