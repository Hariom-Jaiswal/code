class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
        print(f"{value} inserted")

    def dequeue(self):
        if self.is_empty():
            return "Queue Underflow"
        return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Queue:", self.queue)


# Usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

print("Dequeued:", q.dequeue())
print("Front:", q.front())



#Extra
from collections import deque

queue = deque()

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)

# Dequeue
print("Dequeued:", queue.popleft())

# Front element
print("Front:", queue[0])