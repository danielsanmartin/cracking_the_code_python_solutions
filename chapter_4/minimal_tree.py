"""
Minimal Tree: Given a sorted (increasing order) array with unique integer elements, write an
algorithm to create a binary search tree with minimal height.
"""

from graph import TreeBinaryNode


def create_minimal_bst(list_of_numbers, start, end):
    if end < start:
        return None

    middle = int((start + end) / 2)
    node = TreeBinaryNode(list_of_numbers[middle])
    node.left = create_minimal_bst(list_of_numbers, start, middle-1)
    node.right = create_minimal_bst(list_of_numbers, middle+1, end)
    return node


def solution(list_of_numbers) -> TreeBinaryNode:
    return create_minimal_bst(list_of_numbers, 0, len(list_of_numbers)-1)


if __name__ == '__main__':
    numbers = [1, 2, 4, 15, 36]

    head = solution(numbers)
    print(head)
