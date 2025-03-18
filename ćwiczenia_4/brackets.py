import sys

def is_balanced(s):
    stack = [] # lista do przechowywania otwartych nawiasów
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '([{': 
            stack.append(char)
        elif char in ')]}':
            if len(stack)==0 or stack[-1] != pairs[char]:
                return False
            stack.pop() #pop usuwa ostatni element listy
    if len(stack) == 0:
        return True #jeśli nie zostały już żadne niezamknięte nawiasy, to ciąg jest zbalansowany
    else:
        return False
    

def fix_brackets(s):
    stack = [] # lista do przechowywania nawiasów otwartych
    missing_open = 0  # liczba brakujących nawiasów otwartych
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) > 0:
                stack.pop() # zamykamy ostatni otwarty nawias
            else:
                missing_open += 1
    # nawiasy otwarte które pozostały trzeba zamknąć:
    missing_close = len(stack)
    return missing_open + missing_close


def list_brackets(n):
    results = []

    # lista krotek: (aktualny ciąg, liczba nawiasów otwierających, liczba nawiasów zamykających)
    stack = [("", 0, 0)]
    
    while len(stack) > 0:
        brackets, opened, closed = stack.pop() # wyjmujemy ostatnią krotkę ze stack
        # jeśli ciąg ma dłuość 2*n, jest gotowy
        if len(brackets) == 2*n:
            results.append(brackets)
        else:
            # możemy dodać nawias otwierający, jeśli nie przekroczymy limitu n
            if opened < n:
                stack.append((brackets + "(", opened + 1, closed))
            # możemy dodać nawias zamykający, jeśli jest co zamknąć
            if closed < opened:
                stack.append((brackets + ")", opened, closed + 1))
    return results


# wywołanie: python3 brackets.py check '(('
if sys.argv[1] == 'check':
    print(is_balanced(sys.argv[2]))


# wywołanie: python3 brackets.py fix '(('
elif sys.argv[1] == 'fix':
    if fix_brackets(sys.argv[2]) == 0:
        print('Nawiasy są zbalansowane')
    else:
        print('Brakuje ', fix_brackets(sys.argv[2]), ' nawiasów')

# wywołanie: python3 brackets.py list '(('
elif sys.argv[1] == 'list':
    n = int(sys.argv[2])
    print(list_brackets(n))

else:
    print('nieprawidłowy argument')