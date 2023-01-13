"""
Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent.
"""


class TreeNode:

    def __init__(self, value, parent=None):
        self.right = None
        self.left = None
        self.parent = parent
        self.value = value

    def __str__(self):
        return str(self.value)


def get_successor(source_node):
    successor = None
    current_node = source_node

    if not current_node.right and not current_node.parent:
        return current_node
    elif not current_node.right:
        while current_node:
            if current_node.value > source_node.value:
                return current_node
            else:
                current_node = current_node.parent
        return current_node

    elif source_node.right:
        current_node = source_node.right
        while current_node.value > source_node.value:
            if current_node.left:
                current_node = current_node.left
            else:
                break

        return current_node

    return successor


if __name__ == '__main__':

    # The Tree
    #         20
    #      /      \
    #     10       30
    #    /  \     /  \
    #   5   15   25   35
    #      /   \
    #    12    17
    #   /
    #  11


    root = TreeNode(20)
    root.left = n_10 = TreeNode(10, root)
    root.left.left = TreeNode(5, root.left)
    root.left.right = n_15 = TreeNode(15, root.left)
    root.left.right.left = n_12 = TreeNode(12, root.left.right)
    root.left.right.left.left = n_11 = TreeNode(11, root.left.right.left)
    root.left.right.right = n_17 = TreeNode(17, root.left.right)

    root.right = n_30 = TreeNode(30, root)
    root.right.left = n_25 = TreeNode(25, root.right)
    root.right.right = n_35 = TreeNode(35, root.right)

    assert get_successor(n_10) == n_11
    assert get_successor(n_17) == root
    assert get_successor(n_35) is None
    assert get_successor(n_15) == n_17
    assert get_successor(n_12) == n_15
    assert get_successor(n_25) == n_30

