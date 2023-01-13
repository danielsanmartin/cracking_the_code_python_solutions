# Aproach 1: fixed division
class FullStackException(Exception):
    def __str__(self):
        return 'The stack is full'


class EmptyStackException(Exception):
    def __str__(self):
        return 'The stack is empty'


class FixedMultiStack:
    NUMBER_OF_STACKS = 3
    
    def __init__(self, stack_capacity):
        self.sizes = []
        self.values = []
        self.stack_capacity = stack_capacity

    def push(self, stack_num, value) -> None:
        if self.is_full(stack_num):
            raise FullStackException()

        self.sizes[stack_num] += 1
        self.values[self.index_of_top(stack_num)] = value

    def pop(self, stack_num) -> object:
        if self.is_empty(stack_num):
            raise EmptyStackException()

        value = self.values[self.index_of_top(stack_num)]
        self.values[self.index_of_top(stack_num)] = None
        self.sizes[stack_num] -= 1
        return value

    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise EmptyStackException()
        return self.values[self.index_of_top(stack_num)]

    def is_full(self, stack_num) -> bool:
        return self.sizes[stack_num] == self.stack_capacity

    def is_empty(self, stack_num) -> bool:
        return self.sizes[stack_num] == 0

    def index_of_top(self, stack_num):
        return (stack_num * self.stack_capacity) + self.sizes[stack_num] - 1





