"""
Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
projects, where the second project is dependent on the first project). All of a project's dependencies
must be built before the project is. Find a build order that will allow the projects to be built. If there
is no valid build order, return an error.
EXAMPLE
Input:
    projects: a, b, c, d, e, f
    dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output: f, e, a, b, d, c

Solution #2: we can use depth-first search (DFS) to find the build path.
"""
from collections import deque


class Project:
    COMPLETED = 2
    PARTIAL = 1
    BLANK = 0

    def __init__(self, name):
        self.children = []
        self.map = {}
        self.name = name
        self.dependencies = 0
        self.state = self.BLANK

    def add_neighborhood(self, project):
        if project.name not in self.map:
            self.children.append(project)
            self.map.update({project.name: project})
            project.increment_dependencies()

    def increment_dependencies(self):
        self.dependencies += 1

    def decrement_dependencies(self):
        self.dependencies -= 1

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Project({})".format(self.name)


class Graph:

    def __init__(self):
        self.nodes = []
        self.map = {}

    def create_node(self, name):
        node = Project(name)
        self.nodes.append(node)
        self.map[name] = node

    def get_or_create_node(self, name) -> Project:
        if name not in self.map:
            self.create_node(name)
        return self.map[name]

    def add_edge(self, start_name, end_name):
        start = self.get_or_create_node(start_name)
        end = self.get_or_create_node(end_name)
        start.add_neighborhood(end)


def build_graph(projects, dependencies) -> Graph:
    """
    Build the graph, adding the edge (a, b) if b is dependent on a. Assumes a pair
    is listed in "build order". The pair (a, b) in dependencies indicates that b
    depends on a and a must be built before b. */
    """
    graph = Graph()
    for project in projects:
        graph.create_node(project)

    for dependency in dependencies:
        first = dependency[0]
        second = dependency[1]
        graph.add_edge(first, second)

    return graph


def do_dfs(project, stack) -> bool:
    if project.state is Project.PARTIAL:
        return False # there is a cycle

    if project.state is Project.BLANK:
        project.state = Project.PARTIAL
        children = project.children
        for child in children:
            if not do_dfs(child, stack):
                return False
        project.state = Project.COMPLETED
        stack.append(project)

    return True


def order_projects(projects) -> list:
    """
    Return a list of the projects a correct build order
    :param projects: list of projects.
    :return: list of ordered projects.
    """
    order = []
    stack = deque()
    for project in projects:
        if project.state is Project.BLANK:
            if not do_dfs(project, stack):
                return None

    return [project.name for project in stack]


def find_build_order(project_list, dependencies_list) -> list:
    graph = build_graph(project_list, dependencies_list)
    ordered = order_projects(graph.nodes)
    return ordered


if __name__ == '__main__':
    projects = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    dependencies = [('c', 'f'), ('a', 'f'), ('b', 'f'),
                    ('a', 'c'),
                    ('a', 'b'), ('e', 'b'), ('h', 'b'),
                    ('g', 'd')]

    final_order = find_build_order(projects, dependencies)

    print(final_order)
