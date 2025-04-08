class Velocity:
    def __init__(self, beta = 0):
        self.beta = beta
    
    def gamma(self):
        return 1 / (1 - self.beta**2)**0.5
    
    def __add__(self, other): # przeładowanie (overloading) operatora +
        return Velocity((self.beta + other.beta) / (1 + self.beta * other.beta))
    
    def __iadd__(self, other): # przeładowanie operatora +=
        self.beta = (self.beta + other.beta) / (1 + self.beta * other.beta)
        return self
    
    def __repr__(self): # reprezentacja obiektu jako str
        return f"Velocity(beta={round(self.beta, 6)})"
    
    def __str__(self): # uproszczona reprezentacja obiektu jako str - dla użytkownika
        return f"beta = {round(self.beta, 6)}, gamma = {round(self.gamma(), 6)}"  


beta1 = float(input("Podaj beta1: "))
beta2 = float(input("Podaj beta2: "))

v1 = Velocity(beta1)
v2 = Velocity(beta2)
v = v1 + v2
print(v) # print automatycznie wywołuje __str__ które zdefiniowaliśmy

print(repr(v)) # możemy też użyć __repr__