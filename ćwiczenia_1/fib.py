import sys

n = int(sys.argv[1])

def F(n):
    if n == 1 or n==2:
        return 1
    else:
        return F(n-1) + F(n-2)
    
print(F(n))