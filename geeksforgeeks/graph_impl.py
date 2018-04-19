from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Node:
    def __init__(self, name, v):
        self.v = v
        self.name = name
        self.attr = {}

    def __str__(self):
        return "vertex.name=" + self.name

class Edge:
    def __init__(self, n1, n2, attr):
        self.n1 = n1
        self.n2 = n2
        self.attr = {}

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = {}

    def colored_dfs(self, node):
        pass

    def adjacents(self, node):
        return self.edges[node]

    def add_node(self, node):
        self.vertices[node] = node

    def add_edge(self, edge):
        if edge.n1 not in self.edges:
            self.edges[edge.n1] = {}
        self.edges[edge.n1][edge.n2] = edge

        if edge.n2 not in self.edges:
            self.edges[edge.n2] = {}
        self.edges[edge.n2][edge.n1] = edge


# test
g = Graph()
a = Node('A', 1)
b = Node('B', 2)
c = Node('C', 3)

g.add_node(a)
g.add_node(b)
g.add_node(c)
g.add_edge(Edge(a, b, Color.RED))
g.add_edge(Edge(a, c, Color.GREEN))

for _, vertex in g.vertices.items():
    print("adjacents for", vertex)
    for node in g.adjacents(vertex):
        print(node)
