import math

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def printall(self):
        end = '\n' if self.next is None else ' -> '
        print(self.data, end = end)
        if self.next:
            self.next.printall()



def patition(node, x):

    if node is None or node.next is None:
        return False

    head = Node()
    head.next = tail = node
    

    while tail.next is not None:
        if tail.next.data < x:
            tmp = tail.next
            tail.next = tail.next.next

            tmp.next = head.next
            head.next = tmp
        else:
            tail = tail.next

    head = head.next
    return head
 
print('Test 1')

head = Node(3, Node(5,Node(8, Node(5, Node(10, Node(2, Node(1, None)))))))

head.printall()
print('\nPatitioned...')
head = patition(head, 5)
head.printall()

print('\nTest 2')

head2 = Node(36, Node(10,Node(2, Node(5, Node(100, Node(4, Node(7, None)))))))

head2.printall()
print('\nPatitioned...')
head2 = patition(head2, 8)
head2.printall()