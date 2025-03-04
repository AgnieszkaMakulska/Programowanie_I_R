import time

def ifactorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact


def rfactorial(n):
    if n <= 1:
        return 1
    else:
        return n * rfactorial(n-1)
    

n = int(input('Podaj n: '))

i_start = time.perf_counter_ns()
result_i = ifactorial(n)
i_stop = time.perf_counter_ns()

r_start = time.perf_counter_ns()
result_r = rfactorial(n)
r_stop = time.perf_counter_ns()  


print('Wynik iteracyjnie: ' + str(result_i) + ', wykonano w ' + str(i_stop - i_start) + ' ns')
print('Wynik rekurencyjnie: ' + str(result_r) + ', wykonano w ' + str(r_stop - r_start) + ' ns')
    