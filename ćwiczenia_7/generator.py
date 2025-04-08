class LCG:
    def __init__(self, x0, a, b, m):
        #sprawdzamy czy a, m są całkowite i dodatnie, b jest całkowite i nieujemne, a < m, b < m
        if int(m) == m and m > 0 and int(a) == a and a > 0 and int(b) == b and b >= 0 and a < m and b < m:
            self.x0 = x0
            self.a = a
            self.b = b
            self.m = m
            self.x = x0

    def __call__(self): # przeładowanie operatora wywołania ()
        self.x = (self.a * self.x + self.b) % self.m
        return self.x
        
    def min(self): # zakładamy że m > 0
        return 0
    
    def max(self):
        return self.m - 1
    
    
    
# Przykład użycia - tworzymy generator LCG
lcg = LCG(x0=1, a=1103515245, b=12345, m=2**31)

# Generujemy kilka liczb pseudolosowych - dla każdego zbioru (x0,a,b,m) będzie to inny ciąg
print(lcg())
#print(lcg())
#print(lcg())