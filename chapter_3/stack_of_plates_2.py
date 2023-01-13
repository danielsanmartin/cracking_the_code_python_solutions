# Page 234
# 3.3 Stack of Plates
# Implement a function popAt(int index) which performs a pop operation on a specific substack.

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

    def pop_at(self, index):
        return self.left_shift(index, True)

    def get_last_stack(self):
        if len(self.stacks) == 0:
            return None
        return self.stacks[len(self.stacks)-1]

    def is_empty(self):
        last = self.get_last_stack()
        return last is None or last.is_empty()

    def left_shift(self, index, remove_top) -> object:
        stack = self.stacks[index]

        if remove_top:
            removed_item = stack.pop()
        else:
            removed_item = stack.popleft()

        if len(stack) == 0:
            self.stacks.pop(index)
        elif len(self.stacks) > index + 1:
            v = self.left_shift(index+1, False)
            stack.append(v)

        return removed_item


stacks = SetOfStack(2)

stacks.push(1)
stacks.push(2)
stacks.push(3)
stacks.push(4)
stacks.push(5)
stacks.push(6)
stacks.push(7)
stacks.push(8)

print(stacks.stacks)
print(stacks.pop_at(1))
print(stacks.stacks)
