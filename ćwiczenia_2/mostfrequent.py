
def most_frequent(num_list):
    x_frequent = [] # najczęściej występujące wartości
    max_count = 0 # maksymalna liczba wystąpień tej samej wartości

    for x in num_list:
        if num_list.count(x) > max_count:
            max_count = num_list.count(x)

    for x in num_list:
        if (num_list.count(x) == max_count) and (x not in x_frequent):
            x_frequent.append(x)           

    return [(x, max_count) for x in x_frequent] #list comprehension

# metoda split rozdziela "1 2 3" na listę ["1","2","3"]
str_list = input('Podaj liczby całkowite oddzielone spacjami: \n').split() 
num_list = [int(s) for s in str_list] # zmiana str na int

print(most_frequent(num_list))