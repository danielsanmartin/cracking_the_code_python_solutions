class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def printall(self):
        end = '\n' if self.next is None else ' -> '
        print(self.data, end = end)
        if self.next:
            self.next.printall()