import sys

'''
https://en.wikipedia.org/wiki/Stack_(abstract_data_type)

In computer science, a stack is an abstract data type that serves as a collection of elements with two main operations:

Push, which adds an element to the collection, and
Pop, which removes the most recently added element.
Additionally, a peek operation can, without modifying the stack, return the value of the last element added. 
'''

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        '''Dodaje element na szczyt stosu'''
        self.stack.append(value)

    def pop(self):
        '''Usuwa i zwraca element ze szczytu stosu'''
        if self.stack: #jeśli w stosie są elementy
            return self.stack.pop()
        else:
            return None
    
    def peek(self):
        '''Zwraca element ze szczytu stosu'''
        if self.stack: #jeśli w stosie są elementy
            return self.stack[-1]
        else:
            return None


s = Stack()

for arg in sys.argv[1:]:
    s.push(float(arg))

while s.stack: #dopóki stos nie jest pusty
    print(s.pop())