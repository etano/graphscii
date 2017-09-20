from __future__ import print_function
from math import sqrt
from drawille import Canvas
import networkx as nx

class Node(object):
    """Node class

       Attributes:
           x (int): x-position
           y (int): y-position
           label (str): Label
           att (dict(str, val)): Dictionary of attributes
    """

    def __init__(self, x, y, label=""):
        self.x = x
        self.y = y
        self.label = label
        self.att = {}

class Edge(object):
    """Edge class

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

        self.node_width = 30
        self.node_height = 10
        self.max_x = 200
        self.max_y = 100

    def add_node(self, label):
        self.nodes[label] = Node(0, 0, label)

    def add_edge(self, label0, label1, label=""):
        if not (label0 in self.nodes): self.add_node(label0)
        if not (label1 in self.nodes): self.add_node(label1)
        self.edges.append(Edge(self.nodes[label0], self.nodes[label1], label))

    def draw_node(self, n):
        half_width = self.node_width // 2
        half_height = self.node_height // 2
        for i in range(self.node_width):
            self.c.set((n.x - half_width) + i, n.y - half_height)
            self.c.set((n.x - half_width) + i, n.y + half_height)
        for i in range(self.node_height):
            self.c.set(n.x - half_width, (n.y - half_height) + i)
            self.c.set(n.x + half_width, (n.y - half_height) + i)
        label = n.label
        for key in n.att:
            label += ', '+str(n.att[key])
        self.c.set_text(n.x - half_width + 3, n.y, label)

    def draw_edge(self, e):
        x_diff = e.n1.x - e.n0.x
        y_diff = e.n1.y - e.n0.y
        l = sqrt(x_diff**2 + y_diff**2)
        m = (y_diff / x_diff) if x_diff else 0
        dx = x_diff / l if l else 0
        dy = y_diff / l if l else 0
        half_width = self.node_width // 2
        half_height = self.node_height // 2
        for i in range(int(l)):
            x = e.n0.x + i*dx
            y = e.n0.y + i*dy
            if (
                abs(x - e.n0.x) > half_width and
                abs(x - e.n1.x) > half_width
            ) or (
                abs(y - e.n0.y) > half_height and
                abs(y - e.n1.y) > half_height
            ): self.c.set(x, y)
        self.c.set_text(e.n0.x + (l // 2)*dx, e.n0.y + (l // 2)*dy, e.label)

    def draw(self):
        # TODO: Remove networkx
        G = nx.Graph()
        for edge in self.edges:
            G.add_edge(edge.n0.label, edge.n1.label)
        pos = nx.spring_layout(G)

        # Draw
        for label in self.nodes:
            node = self.nodes[label]
            node.x = float(pos[label][0] * self.max_x)
            node.y = float(pos[label][1] * self.max_y)
            self.draw_node(node)
        for edge in self.edges:
            self.draw_edge(edge)
        print(self.c.frame())

g = Graph()
g.add_edge('Alaska', 'Canada')
g.add_edge('Alaska', 'Kamchatka')
g.add_edge('Alaska', 'Western US')
g.add_edge('Western US', 'Eastern US')
g.add_edge('Western US', 'Canada')
g.add_edge('Western US', 'Mexico')
g.add_edge('Eastern US', 'Canada')
g.add_edge('Eastern US', 'Mexico')
g.add_edge('Eastern US', 'Quebec')
g.add_edge('Canada', 'Quebec')
g.add_edge('Quebec', 'Iceland')

# Add armies
for label in g.nodes:
    node = g.nodes[label]
    node.att['owner'] = 'Ethan'
    node.att['armies'] = 13

g.draw()
