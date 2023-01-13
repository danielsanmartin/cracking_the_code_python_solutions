import math

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

    def printall(self):
        print(self.val)
        if self.next:
            self.next.printall()



def delete_middle_note(node):

    if node is None or node.next is None:
        return False

    next = node.next
    node.val = next.val
    node.next = next.next

    return True



first = Node(1, None)
second = Node(2, Node(3,Node(4, Node(5, Node(6, None)))))
first.next = second
first.printall()

delete_middle_note(second)
print('Removed...')
first.printall()