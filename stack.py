class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        print(f"{value} pushed")

    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Stack:", self.stack)


# Usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)

s.display()

print("Popped:", s.pop())
print("Top:", s.peek())




#Extra
from collections import deque

stack = deque()

stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)

print("Popped:", stack.pop())
print("Top element:", stack[-1])