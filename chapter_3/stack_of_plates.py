from collections import deque


class SetOfStack:

    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def push(self, value):
        last = self.get_last_stack()
        if (last is not None) and (len(last) < self.capacity):
            last.append(value)
        else:
            stack = deque()
            stack.append(value)
            self.stacks.append(stack)

    def pop(self):
        last = self.get_last_stack()
        if last is None:
            return None
        else:
            item = last.pop()
            if len(last) == 0:
                self.stacks.pop()
            return item

    def get_last_stack(self):
        if len(self.stacks) == 0:
            return None
        return self.stacks[len(self.stacks)-1]



stacks = SetOfStack(2)

stacks.push(1)
stacks.push(2)
stacks.push(3)
stacks.push(4)
stacks.push(5)

print(stacks.stacks)
print(stacks.pop())
print(stacks.stacks)
