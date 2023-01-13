# Page 237
# 3.5 Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and is Empty.

from stack import Stack


class SortStack:

    def __init__(self):
        self.stack = Stack()
        self.tmp_stack = Stack()

    def push(self, data):
        if self.stack.is_empty() or data < self.stack.peek():
            self.stack.push(data)
            self.__recopy()
        else:
            self.tmp_stack.push(self.stack.pop())
            self.push(data)

    def __recopy(self):
        if not self.tmp_stack.is_empty():
            while not self.tmp_stack.is_empty():
                self.stack.push(self.tmp_stack.pop())


ss = SortStack()
ss.push(3)
print(ss.stack)
ss.push(2)
print(ss.stack)
ss.push(10)
print(ss.stack)
ss.push(19)
print(ss.stack)









