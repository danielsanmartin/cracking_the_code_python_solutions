class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

    def printall(self):
        print(self.val)
        if self.next:
            self.next.printall()


def kth_to_last(node, k):
    
    for i in range(0, k):
        if not node:
            return None 
        node = node.next

    count = 1

    while node.next is not None:
        node = node.next
        count += 1

    return count

first = Node(1, Node(2, Node(3,Node(4, Node(3, None)))))

assert kth_to_last(first, 3) == 2

    