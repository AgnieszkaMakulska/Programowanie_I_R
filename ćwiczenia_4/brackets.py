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
            if open_count > 0:
                open_count -= 1
            else:
                close_count += 1
    return open_count + close_count


if sys.argv[1] == 'check':
    print(is_balanced(sys.argv[2]))

elif sys.argv[1] == 'fix':
    print('Trzeba dopisać ', fix_brackets(sys.argv[2]), 'nawiasów')


else:
    print('nieprawidłowy argument')