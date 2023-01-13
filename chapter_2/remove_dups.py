class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

    def printall(self):
        print(self.val)
        if self.next:
            self.next.printall()


def delete_dups(node):
    uniques = []

    previous = node
    current = node.next

    while current is not None:
        if current.val in uniques:
            previous.next = current.next
        else:
            previous = current
            uniques.append(current.val)

        current = current.next



first = Node(1, Node(2, Node(2,Node(3, Node(3, Node(4, None))))))
first.printall()

delete_dups(first)
print('Removed...')
first.printall()