# To jest inna wersja kodu niż pokazywałam na ćwiczeniach - 
# trochę bardziej optymalna (bez wielokrotnych pętli for).

def most_frequent(num_list):
    unique_values = []  # lista z unikalnymi wartościami
    counts = []  # lista z liczbami powtórzeń

    for x in num_list:
        if x not in unique_values:
            unique_values.append(x)
            counts.append(1)
        else:
            x_index = unique_values.index(x)
            counts[x_index] += 1
            
    max_count = max(counts) # maksymalna liczba powtórzeń

    return [(unique_values[i], max_count) for i in range(len(unique_values)) if counts[i] == max_count] #list comprehension

# metoda split rozdziela "1 2 3" na listę ["1","2","3"]
str_list = input('Podaj liczby całkowite oddzielone spacjami: \n').split() 
num_list = [int(s) for s in str_list] # zmiana str na int

print(most_frequent(num_list))