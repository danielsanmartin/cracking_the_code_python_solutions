# First Common Ancestor: Design an algorithm and write code to find the first common ancestor
# of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
# necessarily a binary search tree.

from graph import TreeBinaryNode


####################################################################################
# Solution 1: with links to parent
def common_ancestor_1(p, q) -> TreeBinaryNode:
    delta = depth(p) - depth(q)
    first = q if delta > 0 else p
    second = p if delta > 0 else q
    second = go_up_to(second, abs(delta))

    while first != second and first is not None and second is not None:
        first = first.parent
        second = second.parent

    return None if first is None or second is None else first


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


####################################################################################
# Solution 2: With Links to Parents (Better Worst-Case Runtime)
def common_ancestor_2(root, p, q) -> TreeBinaryNode:
    #Check if either node is not in the tree, or if one covers the other.
    if not covers(root, p) or not covers(root, q):
        return None
    elif covers(p, q):
        return p
    elif covers(q, p):
        return q

    # Traverse upwards until you find a node that covers q.
    sibling = get_sibling(p)
    parent = p.parent

    while not covers(sibling, q):
        sibling = get_sibling(parent)
        parent = parent.parent
    
    return parent


def covers(root, p) -> bool:
    if root is None:
        return False
    elif root == p:
        return True
    
    return covers(root.left, p) or covers(root.right, p)


def get_sibling(node) -> TreeBinaryNode:
    if node is None or node.parent is None:
        return None
    
    parent = node.parent
    return parent.right if parent.left == node else parent.left


####################################################################################
# Solution #3: Without Links to Parents
def common_ancestor_3(root, p, q) -> TreeBinaryNode:

    # Error check - one node is not in the tree.
    if not covers(root, p) or not covers(root, q):
        return None
    
    return ancestor_helper(root, p, q)


def ancestor_helper(root, p, q) -> TreeBinaryNode:
    if root is None or root == p or root == q:
        return root
    
    p_is_on_left = covers(root.left, p)
    q_is_on_left = covers(root.left, q)

    if p_is_on_left != q_is_on_left: # nodes are in different side
        return root
    
    child_side = root.left if p_is_on_left else root.right

    return ancestor_helper(child_side, p, q)


####################################################################################
# Solution #4: Optimized

class Result:
    def __init__(self, n, is_ancestor) -> None:
        self.node = n
        self.is_ancestor = is_ancestor


def common_ancestor_4(root, p, q) -> TreeBinaryNode:
    r = common_ancestor_helper(root, p, q)
    if r.is_ancestor:
        return r.node
    return None


def common_ancestor_helper(root, p, q) -> Result:
    if root is None:
        return Result(None, False)

    if root == p and root == q:
        return Result(root, True)

    rx = common_ancestor_helper(root.left, p, q)
    if rx.is_ancestor: # Found common ancestor
        return rx

    ry = common_ancestor_helper(root.right, p, q)
    if ry.is_ancestor:
        return ry
    
    if rx.node != None and ry.node != None:
        return Result(root, True)  # this is the common ancestor

    elif root == p or root == q:
        # If we're currently at p or q, and we also found one of those nodes in a
        # subtree, then this is truly an ancestor and the flag should be true.
        is_ancestor = rx.node != None or ry.node != None
        return Result(root, is_ancestor)
    else:
        return Result(rx.node if rx.node != None else ry.node, False)

    

####################################################################################
# MAIN
####################################################################################
if __name__ == '__main__':

    # The Tree
    #         20
    #        /  \
    #      /      \
    #     10       30
    #    /  \     /  \
    #   5   15   25   35
    #      /  \
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


    assert common_ancestor_1(n_5, n_11) == n_10

    assert common_ancestor_2(root, n_5, n_11) == n_10

    assert common_ancestor_3(root, n_5, n_11) == n_10

    assert common_ancestor_4(root, n_5, n_11) == n_10