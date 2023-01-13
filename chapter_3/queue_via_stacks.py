# Page 236
# 3.4 Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.

# Fila é fist in first out
from collections import deque


class Queue:

    def __init__(self):
        self.stack_newest = deque()
        self.stack_oldest = deque()

    def peek(self):
        self.shift_stacks()
        return self.stack_oldest[-1]

    def remove(self):
        self.shift_stacks()
        return self.stack_oldest.pop()

    def add(self, value):
        self.stack_newest.append(value)

    def size(self):
        return len(self.stack_newest) + len(self.stack_oldest)

    def __len__(self):
        return self.size()

    def print(self):
        for e in self.stack_newest:
            print(e)
        for e in self.stack_oldest:
            print(e)

    def shift_stacks(self):
        if len(self.stack_oldest) == 0:
            while len(self.stack_newest) > 0:
                self.stack_oldest.append(self.stack_newest.pop())


q = Queue()
q.add(1)
q.add(2)
q.add(3)
q.add(4)
q.print()
print('--- Size ---')
print(len(q))
print('--- Peek ---')
print(q.peek())
print('--- Remove ---')
q.remove()
q.print()

print('--- Size after remove ---')
print(len(q))