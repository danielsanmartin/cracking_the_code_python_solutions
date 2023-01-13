from collections import deque
import sys


class NodeWithMin:
    def __init__(self, value, min_value):
        self.value = value
        self.min = min_value


class StackWithMin:

    def __init__(self):
        self.stack = deque()

    def push(self, value):
        new_win = (value if value < self.min() else self.min())
        self.stack.append(NodeWithMin(value, new_win))

    def pop(self):
        return self.stack.pop()

    def min(self):
        if len(self.stack) == 0:
            return int(sys.maxsize)
        else:
            return self.stack[-1].min


if __name__ == '__main__':
    stack = StackWithMin()
    stack.push(5)
    stack.push(6)
    stack.push(3)
    stack.push(7)

    print(stack.min())
