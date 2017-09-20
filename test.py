from __future__ import print_function
from drawille import Canvas
from math import sqrt

class Node(object):
    """Class to draw a box

       Attributes:
           x0 (int): Leftmost x-position
           y0 (int): Topmost y-position
           width (int): Width
           height (int): Height
           label (str): Label
    """

    def __init__(self, x0, y0, width, height, label=""):
        self.x0 = x0
        self.y0 = y0
        self.width = width
        self.height = height
        self.label = label

class Edge(object):
    """Class to draw an edge between Nodes

       Attributes:
           n0 (Node): Starting node
           n1 (Node): Ending node
           label (str): Label
    """

    def __init__(self, n0, n1, label=""):
        self.n0 = n0
        self.n1 = n1
        self.label = label

class Graph(object):
    """Graph class

       Attributes:
           nodes (list(Node)): List of nodes
           edges (list(Edge)): List of edges
           c (drawille.Canvas): Canvas object
    """

    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.c = Canvas()

    def add_node(self, label):
        self.nodes[label] = Node((len(self.nodes)*20) % 40, len(self.nodes)*20, 10, 10, label)

    def add_edge(self, label0, label1, label=""):
        self.edges.append(Edge(self.nodes[label0], self.nodes[label1], label))

    def draw_node(self, n):
        for i in range(n.width):
            self.c.set(n.x0 + i, n.y0)
            self.c.set(n.x0 + i, n.y0 + n.height)
        for i in range(n.height):
            self.c.set(n.x0, n.y0 + i)
            self.c.set(n.x0 + n.width, n.y0 + i)
        self.c.set_text(n.x0 + (n.width // 2), n.y0 + (n.height // 2), n.label)

    def draw_edge(self, e):
        x0 = e.n0.x0 + (e.n0.width // 2)
        x1 = e.n1.x0 + (e.n1.width // 2)
        y0 = e.n0.y0 + (e.n0.height // 2)
        y1 = e.n1.y0 + (e.n1.height // 2)
        x_diff = x1-x0
        y_diff = y1-y0
        l = sqrt(x_diff**2 + y_diff**2)
        m = (y_diff / x_diff) if x_diff else 0
        dx = x_diff / l if l else 0
        dy = y_diff / l if l else 0
        for i in range(int(l)):
            x = x0 + i*dx
            y = y0 + i*dy
            if (
                abs(x-x0) > (e.n0.width // 2) and
                abs(x-x1) > (e.n1.width // 2)
            ) or (
                abs(y-y0) > (e.n0.height // 2) and
                abs(y-y1) > (e.n1.height // 2)
            ): self.c.set(x, y)
        self.c.set_text(x0 + (l // 2)*dx, y0 + (l // 2)*dy, e.label)

    def draw(self):
        # TODO: draw to minimize edge crossings
        for label in self.nodes:
            self.draw_node(self.nodes[label])
        for edge in self.edges:
            self.draw_edge(edge)
        print(self.c.frame())

g = Graph()
g.add_node('n0')
g.add_node('n1')
g.add_node('n2')
g.add_node('n3')
g.add_node('n4')
g.add_edge('n0', 'n1', 'e0')
g.add_edge('n0', 'n2', 'e1')
g.add_edge('n2', 'n1', 'e2')
g.draw()
