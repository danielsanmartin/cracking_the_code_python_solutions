"""
Validate BST: Implement a function to check if a binary tree is a binary search tree.
"""


class TreeNode:

    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value


def create_bst_1():
    root = TreeNode(20)
    root.left = TreeNode(10)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(15)
    root.right = TreeNode(30)
    root.right.left = TreeNode(25)
    root.right.right = TreeNode(35)
    return root


def create_bst_2():
    root = TreeNode(20)
    root.left = TreeNode(10)
    return root


def create_bst_1_false():
    root = TreeNode(20)
    root.left = TreeNode(30)
    return root


def create_bst_2_false():
    root = TreeNode(20)
    root.left = TreeNode(10)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(15)
    root.right = TreeNode(30)
    root.right.left = TreeNode(25)
    root.right.right = TreeNode(15)
    return root


def validate_bst(root):
    if root.left is None and root.right is None:
        return True

    left = True
    right = True
    if root.left:
        if root.value > root.left.value:
            left = validate_bst(root.left)
        else:
            return False
    if root.right:
        if root.value < root.right.value:
            right = validate_bst(root.right)
        else:
            return False

    return left and right


print(validate_bst(create_bst_1()))
print(validate_bst(create_bst_2()))
print(validate_bst(create_bst_1_false()))
print(validate_bst(create_bst_2_false()))
