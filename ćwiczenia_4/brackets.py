import sys

def is_balanced(s):
    stack = [] 
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in '([{': 
            stack.append(char)
        elif char in ')]}':
            if len(stack)==0 or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return len(stack) == 0

def fix_brackets(s):
    open_count = 0
    close_count = 0
    for char in s:
        if char == '(':
            open_count += 1
        elif char == ')':
            close_count += 1
    return open_count - close_count


if sys.argv[1] == 'check':
    print(is_balanced(sys.argv[2]))

elif sys.argv[1] == 'fix':
    if fix_brackets(sys.argv[2]) > 0:
        print('Trzeba dodać ', fix_brackets(sys.argv[2]), 'nawiasów )')
    elif fix_brackets(sys.argv[2]) < 0: 
        print('Trzeba dopisać ', -fix_brackets(sys.argv[2]), 'nawiasów (')
    elif fix_brackets(sys.argv[2]) == 0:
        print('Nawiasy są poprawne')


else:
    print('nieprawidłowy argument')