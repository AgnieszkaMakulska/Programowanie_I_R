import sys

def is_palindrome(word):
    if word == word[::-1]:
    # word[start:stop:step] - tutaj start i stop są pominięte, więc wybieramy całą listę z krokiem -1 (od końca)
        return True
    else:
        return False


words_list = sys.argv[1:]
print([word for word in words_list if is_palindrome(word)])
