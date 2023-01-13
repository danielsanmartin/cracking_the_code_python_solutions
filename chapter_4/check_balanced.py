"""
Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.
"""

from graph import TreeBinaryNode


def create_unbalanced_bt_1_level() -> TreeBinaryNode:
    root = TreeBinaryNode(20)

    root.left = TreeBinaryNode(10)
    root.left.left = TreeBinaryNode(5)
    root.left.right = TreeBinaryNode(8)

    root.right = TreeBinaryNode(30)

    return root


def create_unbalanced_bt_2_levels() -> TreeBinaryNode:
    root = TreeBinaryNode(20)

    root.left = TreeBinaryNode(10)
    root.left.left = TreeBinaryNode(5)
    root.left.left.left = TreeBinaryNode(3)

    root.left.right = TreeBinaryNode(8)

    root.right = TreeBinaryNode(30)
    return root


def create_balanced_bt() -> TreeBinaryNode:
    root = TreeBinaryNode(20)
    root.left = TreeBinaryNode(10)
    root.right = TreeBinaryNode(30)

    root.left.left = TreeBinaryNode(5)
    root.left.right = TreeBinaryNode(8)

    root.right.left = TreeBinaryNode(25)
    root.right.right = TreeBinaryNode(35)
    return root


def get_height(root) -> int:
    if root is None:
        return -1
    else:
        return max(get_height(root.left), get_height(root.right))+1


def check_balanced(root) -> bool:
    if root is None:
        return True

    height_diff = get_height(root.left) - get_height(root.right)
    if abs(height_diff) > 1:
        return False
    else:
        return check_balanced(root.left) and check_balanced(root.right)


root = create_unbalanced_bt_1_level()
print(check_balanced(root))

root = create_unbalanced_bt_2_levels()
print(check_balanced(root))

root = create_balanced_bt()
print(check_balanced(root))
