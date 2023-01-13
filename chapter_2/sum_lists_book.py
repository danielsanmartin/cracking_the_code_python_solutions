# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.
#
# Book's solution.

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def printall(self):
        print(self.data)
        if self.next:
            self.next.printall()


def sum_lists(l1, l2, carry):
    
    if l1 is None and l2 is None and carry == 0:
        return None

    result = Node(None, None)
    
    value = carry
    if l1 is not None:
        value += l1.data
    if l2 is not None:
        value += l2.data

    result.data = value % 10 # second number

    if l1 is not None or l2 is not None:
        more = sum_lists(None if l1 is None else l1.next,
            None if l2 is None else l2.next,
            1 if value >= 10 else 0)

        result.next = more

    return result
 


l1 = Node(7, Node(7,Node(8, None)))
l2 = Node(9, Node(9,Node(8, None)))

head = sum_lists(l1, l2, 0)

print(head.printall())