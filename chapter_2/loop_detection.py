# Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
# as to make a loop in the linked list.
# EXAMPLE
# Input: A - > B - > C - > D - > E - > C [the same C as earlier]
# Output: C




class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return str(self.data)

    def printall(self):
        print(self.data)
        if self.next:
            self.next.printall()


def detect_loop(head):
    slow = head
    fast = head

    while slow != None and fast != None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    # Error check - no meeting point, and therefore no loop
    if fast == None or fast.next == None:
        return None
    
    # Move slow to Head. Keep fast at Meeting Point. Each are k steps from the
    # Loop Start. If they move at the same pace, they must meet at Loop Start.
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return fast
 


e = Node('E')
d = Node('D')
c = Node('C')
b = Node('B')
a = Node('A')
a.next = b
b.next = c
c.next = d
d.next = e
e.next = c

node = detect_loop(a)

print(node)