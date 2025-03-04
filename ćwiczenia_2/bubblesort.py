def bubble_sort(num_list):
    n = len(num_list)
    while True:
        swapped = False
        for i in range(n-1): # przechodzimy po kolejnych elementach listy
            if num_list[i] > num_list[i+1]: #jeżeli są ustawione w złej kolejności, zostają zamienione miejscami
                num_list[i], num_list[i+1] = num_list[i+1], num_list[i]
                swapped = True
        if not swapped:
            break
        n = n-1 # ta linijka nie jest konieczna, ale dzięki niej unikamy sprawdzania wielokrotnie tych samych elementów

    return num_list


num_list = [int(s) for s in input('Podaj liczby całkowite oddzielone spacjami: \n').split()]
print('Posortowana lista: ', bubble_sort(num_list))