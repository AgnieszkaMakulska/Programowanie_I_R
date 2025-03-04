import sys

n = int(sys.argv[1])

def F(n):
    if n == 1 or n==2:
        return 1
    else:
        return F(n-1) + F(n-2)
    
sum = 0
for i in range(1,n+1):
    F_i = F(i)
    if i%2 == 0 and F_i < 3e6:
        print('i=' + str(i) + ' F(i) = '+ str(F_i))
        sum += F_i
print('sum = ' + str(sum))