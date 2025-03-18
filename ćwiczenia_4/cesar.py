import sys

def cesar(n, text):
    result = []
    for char in text:
        if char.isalpha():  # sprawdzamy czy znak jest literą
            if char.islower():
            # ord() zwraca kod ASCII danego znaku
            # chr() zwraca znak o danym kodzie ASCII
                result.append(chr( ord('a') + (ord(char) - ord('a') + n) % 26 ))
            elif char.isupper():
                result.append(chr( ord('A') + (ord(char) - ord('A') + n) % 26 ))
        else:
            result.append(char) 
    return ''.join(result)

if len(sys.argv) != 4:
    print("nieprawidłowa liczba argumentów")

n = int(sys.argv[2])
text = sys.argv[3]

if sys.argv[1] == 'encrypt':
    print(cesar(n, text))

elif sys.argv[1] == 'decrypt':
     print(cesar(-n, text))

#wywołanie: python3 cesar.py encrypt 3 'Programowanie13w@$Pythonie'
