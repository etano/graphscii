from __future__ import print_function
from math import sqrt
from drawille import Canvas

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

        self.max_x = 300
        self.max_y = 125

    def add_node(self, label, x=0, y=0):
        self.nodes[label] = Node(x, y, label)

    def add_edge(self, label0, label1, label=""):
        if not (label0 in self.nodes): self.add_node(label0)
        if not (label1 in self.nodes): self.add_node(label1)
        self.edges.append(Edge(self.nodes[label0], self.nodes[label1], label))

    def draw_node(self, n, width, height):
        half_width = width // 2
        half_height = height // 2
        for i in range(width):
            self.c.set((n.x - half_width) + i, n.y - half_height)
            self.c.set((n.x - half_width) + i, n.y + half_height)
        for i in range(height):
            self.c.set(n.x - half_width, (n.y - half_height) + i)
            self.c.set(n.x + half_width, (n.y - half_height) + i)
        label = n.label
        for key in n.att:
            label += ', '+str(n.att[key])
        self.c.set_text(n.x - half_width + 3, n.y, label)

    def draw_edge(self, e, node_width, node_height):
        x_diff = e.n1.x - e.n0.x
        y_diff = e.n1.y - e.n0.y
        l = sqrt(x_diff**2 + y_diff**2)
        m = (y_diff / x_diff) if x_diff else 0
        dx = x_diff / l if l else 0
        dy = y_diff / l if l else 0
        half_width = node_width // 2
        half_height = node_height // 2
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

    def draw(self, node_width = 30, node_height = 10):
        for label in self.nodes:
            node = self.nodes[label]
            node.x = float(node.x * self.max_x)
            node.y = float(node.y * self.max_y)
            self.draw_node(node, node_width, node_height)
        for edge in self.edges:
            self.draw_edge(edge, node_width, node_height)
        print(self.c.frame())

def get_risk_graph():
    g = Graph()

    # North America
    g.add_node('Alaska', 0, 0)
    g.add_node('Northwest Territory', 0.1, 0.1)
    g.add_node('Greenland', 0.3, 0.05)
    g.add_node('Alberta', 0.05, 0.2)
    g.add_node('Ontario', 0.15, 0.3)
    g.add_node('Quebec', 0.25, 0.25)
    g.add_node('Western US', 0.05, 0.4)
    g.add_node('Eastern US', 0.25, 0.45)
    g.add_node('Central America', 0.15, 0.6)
    g.add_edge('Alaska', 'Northwest Territory')
    g.add_edge('Alaska', 'Alberta')
    g.add_edge('Northwest Territory', 'Alberta')
    g.add_edge('Northwest Territory', 'Ontario')
    g.add_edge('Northwest Territory', 'Greenland')
    g.add_edge('Alberta', 'Ontario')
    g.add_edge('Alberta', 'Western US')
    g.add_edge('Ontario', 'Greenland')
    g.add_edge('Ontario', 'Quebec')
    g.add_edge('Ontario', 'Western US')
    g.add_edge('Ontario', 'Eastern US')
    g.add_edge('Greenland', 'Quebec')
    g.add_edge('Western US', 'Eastern US')
    g.add_edge('Western US', 'Central America')
    g.add_edge('Quebec', 'Eastern US')

    # South America
    g.add_node('Venezuela', 0.2, 0.7)
    g.add_node('Brazil', 0.3, 0.85)
    g.add_node('Peru', 0.15, 0.8)
    g.add_node('Argentina', 0.2, 1.0)
    g.add_edge('Venezuela', 'Brazil')
    g.add_edge('Venezuela', 'Peru')
    g.add_edge('Brazil', 'Peru')
    g.add_edge('Brazil', 'Argentina')
    g.add_edge('Peru', 'Argentina')

    # Africa
    g.add_node('North Africa', 0.45, 0.65)
    g.add_node('Egypt', 0.55, 0.6)
    g.add_node('East Africa', 0.65, 0.7)
    g.add_node('Congo', 0.5, 0.8)
    g.add_node('South Africa', 0.55, 1.0)
    g.add_node('Madagascar', 0.6, 0.9)
    g.add_edge('North Africa', 'Egypt')
    g.add_edge('North Africa', 'East Africa')
    g.add_edge('North Africa', 'Congo')
    g.add_edge('Egypt', 'East Africa')
    g.add_edge('East Africa', 'Congo')
    g.add_edge('East Africa', 'Madagascar')
    g.add_edge('Congo', 'South Africa')
    g.add_edge('Madagascar', 'South Africa')

    # Europe
    g.add_node('Western Europe', 0.45, 0.5)
    g.add_node('Southern Europe', 0.6, 0.45)
    g.add_node('Northern Europe', 0.55, 0.35)
    g.add_node('Great Britain', 0.4, 0.3)
    g.add_node('Iceland', 0.4, 0.2)
    g.add_node('Scandinavia', 0.55, 0.1)
    g.add_node('Ukraine', 0.6, 0.2)
    g.add_edge('Western Europe', 'Southern Europe')
    g.add_edge('Western Europe', 'Northern Europe')
    g.add_edge('Western Europe', 'Great Britain')
    g.add_edge('Southern Europe', 'Northern Europe')
    g.add_edge('Southern Europe', 'Ukraine')
    g.add_edge('Northern Europe', 'Great Britain')
    g.add_edge('Northern Europe', 'Ukraine')
    g.add_edge('Northern Europe', 'Scandinavia')
    g.add_edge('Great Britain', 'Scandinavia')
    g.add_edge('Great Britain', 'Iceland')
    g.add_edge('Ukraine', 'Scandinavia')
    g.add_edge('Scandinavia', 'Iceland')

    # Asia
    g.add_node('Middle East', 0.7, 0.55)
    g.add_node('Afghanistan', 0.75, 0.4)
    g.add_node('India', 0.8, 0.6)
    g.add_node('Ural', 0.75, 0.15)
    g.add_node('China', 0.9, 0.5)
    g.add_node('Siberia', 0.8, 0.2)
    g.add_node('Mongolia', 0.95, 0.4)
    g.add_node('Yakutsk', 0.85, 0.1)
    g.add_node('Irkutsk', 0.9, 0.25)
    g.add_node('Kamchatka', 1.0, 0.0)
    g.add_node('Japan', 1.0, 0.2)
    g.add_node('Siam', 0.9, 0.65)
    g.add_edge('Middle East', 'Afghanistan')
    g.add_edge('Middle East', 'India')
    g.add_edge('Afghanistan', 'India')
    g.add_edge('Afghanistan', 'Ural')
    g.add_edge('Afghanistan', 'China')
    g.add_edge('India', 'China')
    g.add_edge('India', 'Siam')
    g.add_edge('Ural', 'China')
    g.add_edge('Ural', 'Siberia')
    g.add_edge('China', 'Siam')
    g.add_edge('China', 'Siberia')
    g.add_edge('China', 'Mongolia')
    g.add_edge('Siberia', 'Mongolia')
    g.add_edge('Siberia', 'Yakutsk')
    g.add_edge('Siberia', 'Irkutsk')
    g.add_edge('Mongolia', 'Irkutsk')
    g.add_edge('Mongolia', 'Kamchatka')
    g.add_edge('Mongolia', 'Japan')
    g.add_edge('Yakutsk', 'Irkutsk')
    g.add_edge('Yakutsk', 'Kamchatka')
    g.add_edge('Irkutsk', 'Kamchatka')
    g.add_edge('Kamchatka', 'Japan')

    # Australia
    g.add_node('Indonesia', 0.95, 0.7)
    g.add_node('New Guinea', 1.0, 0.8)
    g.add_node('Western Australia', 0.9, 0.9)
    g.add_node('Eastern Australia', 1.0, 1.0)
    g.add_edge('Indonesia', 'New Guinea')
    g.add_edge('Indonesia', 'Western Australia')
    g.add_edge('New Guinea', 'Western Australia')
    g.add_edge('New Guinea', 'Eastern Australia')
    g.add_edge('Western Australia', 'Eastern Australia')

    # Connections
    g.add_edge('Siam', 'Indonesia')
    g.add_edge('Southern Europe', 'Middle East')
    g.add_edge('Ukraine', 'Ural')
    g.add_edge('Ukraine', 'Afghanistan')
    g.add_edge('Ukraine', 'Middle East')
    g.add_edge('North Africa', 'Western Europe')
    g.add_edge('North Africa', 'Southern Europe')
    g.add_edge('Egypt', 'Middle East')
    g.add_edge('Egypt', 'Southern Europe')
    g.add_edge('East Africa', 'Middle East')
    g.add_edge('Brazil', 'North Africa')
    g.add_edge('Eastern US', 'Central America')
    g.add_edge('Alaska', 'Kamchatka')
    g.add_edge('Greenland', 'Iceland')
    g.add_edge('Central America', 'Venezuela')

    return g

g = get_risk_graph()

# Add armies
for label in g.nodes:
    node = g.nodes[label]
    node.att['owner'] = 'Ethan'
    node.att['armies'] = 13

g.draw(0, 0)
