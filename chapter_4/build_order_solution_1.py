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

Solution #1
"""


class Project:

    def __init__(self, name):
        self.children = []
        self.map = {}
        self.name = name
        self.dependencies = 0

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


def order_projects(projects) -> list:
    """
    Return a list of the projects a correct build order
    :param projects: list of projects.
    :return: list of ordered projects.
    """
    order = []

    # Add "roots" to the build order first
    end_of_list = add_non_dependent(order, projects, 0)

    to_be_processed = 0
    while to_be_processed < len(order):
        current = order[to_be_processed]

        # We have a circular dependency since there are no remaining  projects with zero dependencies.
        if current is None:
            return None

        # Remove myself as a dependency.
        children = current.children
        for child in children:
            child.decrement_dependencies()

        # Add children that have no one depending on them.
        end_of_list = add_non_dependent(order, children, end_of_list)
        to_be_processed += 1

    return [project.name for project in order]


def add_non_dependent(order_list, project_list, offset) -> int:
    for project in project_list:
        if project.dependencies == 0:
            order_list.append(project)
            offset += 1

    return offset


def find_build_order(project_list, dependencies_list) -> list:
    graph = build_graph(project_list, dependencies_list)
    ordered = order_projects(graph.nodes)
    return ordered


if __name__ == '__main__':
    projects = ['a', 'b', 'c', 'd', 'e', 'f']
    dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

    final_order = find_build_order(projects, dependencies)

    assert final_order == ['f', 'e', 'a', 'b', 'd', 'c'] or final_order == ['e', 'f', 'b', 'a', 'd', 'c']
