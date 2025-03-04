import math
import sys

def bubble_sort(num_list):
    n = len(num_list)
    while True:
        swapped = False
        for i in range(n-1):
            if num_list[i] > num_list[i+1]:
                num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
                swapped = True
        if not swapped:
            break
        n = n-1
    return num_list

def bin_search(n_search, num_list, min, max):
    
    sorted_list  = bubble_sort(num_list)
    print('Posortowana lista ', sorted_list)
    L = min
    R = max
    while L <= R:
        m = math.floor((L + R) / 2)
        if sorted_list[m] < n_search:
            L = m + 1
        elif sorted_list[m] > n_search:
            R = m - 1
        elif sorted_list[m] == n_search:
            return m
    print('Nie znaleziono liczby ', n_search, 'pomiędzy indeksami ',min,' a ',max)
    return (-1)

n = int(sys.argv[1])
num_list = [int(s) for s in input('Podaj liczby całkowite oddzielone spacjami: \n').split()]

min = 0
max = len(num_list) #//2
result = bin_search(n,num_list,min,max)

if result != -1:
    print('Indeks ', n, ' w posortowanej rosnąco liście: ', result)

