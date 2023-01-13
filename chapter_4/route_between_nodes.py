"""
Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
"""

from collections import deque
from graph import *


class GNode (Node):
    UNVISITED = 0
    VISITING = 1
    VISITED = 2

    def __init__(self, name=''):
        self.state = self.UNVISITED
        super().__init__(name)


def build_graph(node_a, node_b) -> Graph:
    g = Graph()

    for i in range(0, 5):
        node_a.adjacents.append(GNode('n1{}'.format(i)))
        node_b.adjacents.append(GNode('n2{}'.format(i)))

    g.nodes.append(node_a)
    node_a.adjacents[0].adjacents.append(node_b)

    return g


def search(node_a, node_b) -> bool:

    if node_a == node_b:
        return True

    q = deque()
    node_a.state = GNode.VISITING
    q.append(node_a)

    while len(q) != 0:
        u = q.popleft()
        for v in u.adjacents:
            if v.state == GNode.UNVISITED:
                print(v)
                if v == node_b:
                    return True
                else:
                    v.state = GNode.VISITING
                    q.append(v)
        u.state = GNode.VISITED
    return False


n1 = GNode('n1')
n2 = GNode('n2')
graph = build_graph(n1, n2)

print(search(n1, n2))


