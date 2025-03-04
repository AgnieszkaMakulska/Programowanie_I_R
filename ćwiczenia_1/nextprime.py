import math
#    Wykorzystano algorytm opisany na Wikipedii:
#       https://en.wikipedia.org/wiki/Primality_test#Simple_methods

def is_prime(n):
    if n <= 1: 
        return False
    elif n <= 3: 
        return True
    elif n % 2 == 0 or n % 3 == 0: 
        return False
    i = 5
    # Sprawdzamy czy n jest podzielne przez kolejne liczby pierwsze pomiędzy 5 a sqrt(n).
    while i <= math.sqrt(n):
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def next_prime(n):
    if (n <= 1): return 2

    k = n
    prime = False
    while not prime:
        k += 1
        prime = is_prime(k)

    return k

n = int(input("Podaj liczbę naturalną: "))
print(f"Najmniejsza liczba pierwsza większa od {n} to {next_prime(n)}.")