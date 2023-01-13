# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
# Output: 2 -> 1 -> 9. That is, 912.

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

    def printall(self):
        print(self.val)
        if self.next:
            self.next.printall()


def sum_lists(l1, l2):
    
    extra = 0
    head = last = Node(0, None)

    while l1 or l2:        

        # somando
        sum = l1.val if l1 else 0
        sum += l2.val if l2 else 0
        sum += extra
        if sum > 9:
            extra = 1
            sum = sum - 10
        else:
            extra = 0

        node = Node(sum, None)
        
        # incluindo o valor
        if head.next is None:
            head.next = node
        else:
            last = last.next
            last.next = node

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    if extra:
        last.next.next = Node(extra, None)

    head = head.next

    return head
 


l1 = Node(7, Node(7,Node(8, None)))
l2 = Node(9, Node(9,Node(8, None)))

head = sum_lists(l1, l2)

print(head.printall())