# First Common Ancestor: Design an algorithm and write code to find the first common ancestor
# of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
# necessarily a binary search tree.

from graph import TreeBinaryNode


def depth(node) -> int:
    depth = 0
    while node is not None:
        node = node.parent
        depth += 1
    return depth


def go_up_to(node, delta) -> TreeBinaryNode:
    while delta > 0 and node is not None:
        node = node.parent
        delta -= 1
    return node


# solution 1: with links to parent
def common_ancestor(p, q) -> TreeBinaryNode:
    delta = depth(p) - depth(q)
    first = q if delta > 0 else p
    second = p if delta > 0 else q
    second = go_up_to(second, abs(delta))

    while first != second and first is not None and second is not None:
        first = first.parent
        second = second.parent

    return None if first is None or second is None else first



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


    assert common_ancestor(n_5, n_11) == n_10