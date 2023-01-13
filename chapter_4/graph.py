

class Node:

    def __init__(self, name=''):
        self.name = name
        self.adjacents = []

    def __str__(self):
        return self.name


class TreeBinaryNode:

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


class Graph:
    def __init__(self):
        self.nodes = []



