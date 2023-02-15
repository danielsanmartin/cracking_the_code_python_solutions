# 4.9 BST Sequences: A binary search tree was created by traversing through an array from left to right
# and inserting each element. Given a binary search tree with distinct elements, print all possible
# arrays that could have led to this tree.

from graph import TreeBinaryNode


def all_sequences(node) -> TreeBinaryNode:
    result = []

    if node is None:        
        return [result]

    prefix = []
    prefix.append(node.value)

    # Recurse on left and right subtrees.
    left_seq = all_sequences(node.left)
    right_seq = all_sequences(node.right)

    # Weave together each list from the left and right sides.
    for left in left_seq:
        for right in right_seq:
            weaved = []
            weave_lists(left, right, weaved, prefix)
            result.extend(weaved)
    if not result:
        result.append(prefix)

    return result

# Weave lists together in all possible ways. This algorithm works by removing the
# head from one list, recursing, and then doing the same thing with the other
# list. 
def weave_lists(first, second, results, prefix):
    
    # One list is empty. Add remainder to [a cloned] prefix and store result.
    if len(first) == 0 or len(second) == 0:
        result = prefix.copy()
        result.extend(first)
        result.extend(second)
        results.append(result)
        return

    # Recurse with head of first added to the prefix. Removing the head will damage
    # first, so we'll need to put it back where we found it afterwards.
    head_first = first.pop(0)
    prefix.append(head_first)
    weave_lists(first, second, results, prefix)
    prefix.pop()
    first.insert(0, head_first)


    # Do the same thing with second, damaging and then restoring the list.
    head_second = second.pop(0)
    prefix.append(head_second)
    weave_lists(first, second, results, prefix)
    prefix.pop()
    second.insert(0, head_second)



if __name__ == '__main__':
    # The Tree
    #         20
    #       /    \
    #      /      \
    #     10       30
    #    /  \     /  \
    #   5   15   25   35
    #      /   \
    #    12    17
    #   /
    #  11

    root = TreeBinaryNode(20)
    root.left = n_10 = TreeBinaryNode(10, root)
    root.left.left = n_5 = TreeBinaryNode(5, root.left)
    root.left.right = n_15 = TreeBinaryNode(15, root.left)
    root.left.right.left = n_12 = TreeBinaryNode(12, root.left.right)
    root.left.right.left.left = n_11 = TreeBinaryNode(11, root.left.right.left)
    root.left.right.right = n_17 = TreeBinaryNode(17, root.left.right)

    root.right = n_30 = TreeBinaryNode(30, root)
    root.right.left = n_25 = TreeBinaryNode(25, root.right)
    root.right.right = n_35 = TreeBinaryNode(35, root.right)
    
    result = all_sequences(root)
    print(result)