words_list = input('Podaj oddzielone spacjami wyrazy:\n').split() 

# Zliczanie przy użyciu słownika
# Słownik będzie zawierał pary {słowo : liczba powtórzeń}
dict = {}

for word in words_list:
    if word not in dict:
        dict[word] = 1
    else:
        dict[word] += 1

print(dict)

# Sortowanie słów alfabetycznie
for word in sorted(dict): # sorted() zwraca listę posortowanych alfabetycznie kluczy
    print(word, dict[word])