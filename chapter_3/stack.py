
class Stack:

    class StackNode:
        def __init__(self, data = None):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = self.StackNode()
        self.count = 0

    def pop(self):
        if self.top is None:
            raise Exception('Stack empty')

        self.count -= 1
        data = self.top.data
        self.top = self.top.next
        return data

    def push(self, data):
        self.count += 1

        if self.top is None:
            self.top.data = data
        else:
            new_node = self.StackNode(data)
            new_node.next = self.top
            self.top = new_node

    def peek(self):
        if self.top is None:
            raise Exception('Stack empty')
        return self.top.data

    def is_empty(self):
        return self.top.data is None

    def __str__(self):
        result = []
        node = self.top
        while node.next is not None:
            result.append(str(node.data))
            node = node.next
        return ' '.join(result)