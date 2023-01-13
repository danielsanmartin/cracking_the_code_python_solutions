"""
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
"""

from minimal_tree import solution


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def printall(self):
        end = '\n' if self.next is None else ' -> '
        print(self.data, end = end)
        if self.next:
            self.next.printall()


def create_level_linkedlist(root, lists, level):
    if root is None:
        return None

    list_of_nodes = None
    if len(lists) == level:
        list_of_nodes = Node()
        lists.append(list_of_nodes)
    else:
        list_of_nodes = lists[level]
    list_of_nodes.next = root
    create_level_linkedlist(root.left, lists, level + 1);
    create_level_linkedlist(root.right, lists, level + 1);


def list_of_depths(root):
    linked_lists = []
    create_level_linkedlist(root, linked_lists, 0)
    return linked_lists


if __name__ == '__main__':

    numbers = [1, 2, 4, 15, 36]
    root = solution(numbers)
    lists = list_of_depths(root)
    print(lists)

