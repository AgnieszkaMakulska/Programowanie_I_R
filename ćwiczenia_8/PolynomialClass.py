class Polynomial:

    def __init__(self, c): # c to lista współczynników
        self.c = c

    def Deg(self): # stopień wielomianu
        return len(self.c) - 1
    
    def __getitem__(self, i):
        '''
        Zwraca współczynnik wielomianu. Przykład:
        p = Polynomial([1, 2, 3])
        print(p[0])
        '''
        return self.c[i]
                            
    
    def __setitem__(self, i, value):
        '''
        Zmienia współczynnik wielomianu. Przykład:
        p = Polynomial([1, 2, 3])
        p[1] = 5
        '''
        self.c[i] = value
    
    def __call__(self, x):
        '''
        Zwraca wartość wielomianu od x. Przykład:
        p = Polynomial([1, 2, 3])
        print(p(2))
        '''
        return sum([self.c[i] * x**i for i in range(len(self.c))])
    
    def __add__(self, other):
        max_len = max(len(self.c), len(other.c))
        # dołączamy zera na końcu krótszego wielomianu, żeby miały tą samą długość
        c1 = self.c + [0 for _ in range (max_len - len(self.c))]
        c2 = other.c + [0 for _ in range (max_len - len(other.c))]
        return Polynomial([c1[i] + c2[i] for i in range(max_len)])
    
    def __mul__(self, number): # mnożenie wielomian * licza
        return Polynomial([self.c[i] * number for i in range(len(self.c))])
    
    def __rmul__(self, number): # mnożenie liczba * wielomian
        return Polynomial([self.c[i] * number for i in range(len(self.c))])
    
    def D(self): # pochodna wielomianu
        if len(self.c) <= 1:
            return Polynomial([0])  # pochodna stałej wynosi 0
        else:
            return Polynomial([self.c[i] * i for i in range(1, len(self.c))])
  

    

