from linkedlist import Node

def create_reverse_copy(node) -> Node:
    head = tail = Node(node.data)

    while node.next:
        tmp = head
        head = Node(node.next.data)
        head.next = tmp
        node = node.next

    return head

def is_palindrome(node) -> bool:
    reverse = create_reverse_copy(node)

    while node:
        if node.data != reverse.data:
            return False

        node = node.next
        reverse = reverse.next

    return True


print('Test Reverse Function')
original = Node(3, Node(5,Node(8, Node(5, Node(10, Node(2, Node(1, None)))))))
original.printall()
result = create_reverse_copy(original)
result.printall()

print('\n')

print('Test 1. Expected: False')
not_palindrome = Node(3, Node(5,Node(8, Node(5, Node(10, Node(2, Node(1, None)))))))
not_palindrome.printall()
result = is_palindrome(not_palindrome)
print('Result: ',result)

print('\nTest 2. Expected: True')
palindrome1 = Node(1, Node(2,Node(3, Node(3, Node(2, Node(1,None))))))
palindrome1.printall()
result = is_palindrome(palindrome1)
print('Result: ',result)

print('\nTest 3. Expected: True')
palindrome1 = Node(1, Node(2,Node(3, Node(5, Node(3, Node(2, Node(1,None)))))))
palindrome1.printall()
result = is_palindrome(palindrome1)
print('Result: ',result)