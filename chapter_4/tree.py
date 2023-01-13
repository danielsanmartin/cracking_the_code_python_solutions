class Node:
    def __init__(self, name=''):
        self.name = name
        self.children = []  # others nodes


class Tree:
    def __init__(self):
        self.root = Node()