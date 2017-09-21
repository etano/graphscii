from __future__ import print_function
from math import sqrt
from drawille import Canvas

class Node(object):
    """Node class

       Attributes:
           label (str): Label for the node
           att (dict(str, val)): Dictionary of attributes for the node
           pos (list(float)): x, y position between 0 and 1
           shape (list(float)): Shape of node
           show_label (bool): Whether or not to show the label
           show_att (bool): Whether or not to show the attributes
    """

    def __init__(self, label, att={}, pos=[0, 0], shape=[10, 10], show_label=True, show_att=False):
        """Initialize Node class

           Args:
               label (str): Label for the node
               att (dict(str, val)): Dictionary of attributes for the node
               pos (list(float)): x, y position between 0 and 1
               shape (list(float)): Shape of node
               show_label (bool): Whether or not to show the label
               show_att (bool): Whether or not to show the attributes
        """
        if len(pos) != 2: raise ValueError('pos must be of length 2')
        if pos[0] < 0 or pos[0] > 1: raise ValueError('x position must be between 0 and 1')
        if pos[1] < 0 or pos[1] > 1: raise ValueError('y position must be between 0 and 1')
        if len(shape) != 2: raise ValueError('shape must be of length 2')
        self.label = label
        self.att = dict(att)
        self.pos = list(pos)
        self.shape = list(shape)
        self.show_label = show_label
        self.show_att = show_att

class Edge(object):
    """Edge class

       Attributes:
           n0 (Node): Starting node
           n1 (Node): Ending node
           label (str): Label
           att (dict(str, val)): Dictionary of attributes
           show_label (bool): Whether or not to show the label
           show_att (bool): Whether or not to show the attributes
    """

    def __init__(self, n0, n1, label, att, show_label=True, show_att=False):
        """Initialize Edge class

           Args:
               n0 (Node): Starting node
               n1 (Node): Ending node
               label (str): Label
               att (dict(str, val)): Dictionary of attributes
               show_label (bool): Whether or not to show the label
               show_att (bool): Whether or not to show the attributes
        """
        self.n0 = n0
        self.n1 = n1
        self.label = label
        self.att = dict(att)
        self.show_label = show_label
        self.show_att = show_att

class Graph(object):
    """Graph class

       Attributes:
           max_x (int): Maximum horizontal canvas size
           max_y (int): Maximum vertical canvas size
           default_shape (list(float)): Default node shape
           nodes (dict(str, Node)): Dictionary of nodes
           edges (list(Edge)): List of edges
    """

    def __init__(self, max_x=300, max_y=135, default_shape=[10, 10]):
        """Initialize Graph

           Args:
               max_x (int): Maximum horizontal canvas size
               max_y (int): Maximum vertical canvas size
               default_shape (list(float)): Default node shape
        """
        self.max_x = max_x
        self.max_y = max_y
        self.default_shape = list(default_shape)
        self.nodes = {}
        self.edges = []

    def add_node(self, label, att={}, pos=[0, 0], shape=None, show_label=True, show_att=False):
        """Add a node

           Args:
               label (str): Label for the node
               att (dict(str, val)): Dictionary of attributes for the node
               pos (list(float)): x, y position between 0 and 1
               shape (list(float)): Shape of node
               show_label (bool): Whether or not to show the label
               show_att (bool): Whether or not to show the attributes
        """
        if not shape:
            shape = self.default_shape
        self.nodes[label] = Node(label, att, pos, shape, show_label, show_att)

    def add_edge(self, label0, label1, label='', att={}, show_label=True, show_att=False):
        """Add an edge

           Args:
               label0 (str): Label for the starting node
               label1 (str): Label for the ending node
               label (str): Label for the edge
               att (dict(str, val)): Dictionary of attributes for the edge
               show_label (bool): Whether or not to show the label
               show_att (bool): Whether or not to show the attributes
        """
        if not (label0 in self.nodes): raise ValueError(label0+' does not exist.')
        if not (label1 in self.nodes): raise ValueError(label1+' does not exist.')
        self.edges.append(Edge(self.nodes[label0], self.nodes[label1], label, att, show_label, show_att))

    def draw_node(self, c, n):
        """Add a node to the canvas

           Args:
               c (drawille.Canvas): Canvas object
               n (Node): Node to draw
        """
        x = float(n.pos[0] * self.max_x)
        y = float(n.pos[1] * self.max_y)
        half_width = n.shape[0] // 2
        half_height = n.shape[1] // 2
        for i in range(n.shape[0]):
            c.set((x - half_width) + i, y - half_height)
            c.set((x - half_width) + i, y + half_height)
        for i in range(n.shape[1]):
            c.set(x - half_width, (y - half_height) + i)
            c.set(x + half_width, (y - half_height) + i)
        label = ''
        if n.show_label:
            label += n.label
        if n.show_att:
            for key in n.att:
                label += ', %s: %s'%(key, str(n.att[key]))
        c.set_text(x - half_width + 3, y, label)

    def draw_edge(self, c, e):
        """Add an edge to the canvas

           Args:
               c (drawille.Canvas): Canvas object
               e (Edge): Edge to draw
        """
        x0 = float(e.n0.pos[0] * self.max_x)
        y0 = float(e.n0.pos[1] * self.max_y)
        x1 = float(e.n1.pos[0] * self.max_x)
        y1 = float(e.n1.pos[1] * self.max_y)
        half_width0 = e.n0.shape[0] // 2
        half_width1 = e.n1.shape[0] // 2
        half_height0 = e.n0.shape[1] // 2
        half_height1 = e.n1.shape[1] // 2
        x_diff = x1 - x0
        y_diff = y1 - y0
        l = sqrt(x_diff**2 + y_diff**2)
        dx = x_diff / l if l else 0
        dy = y_diff / l if l else 0
        for i in range(int(l)):
            x = x0 + i*dx
            y = y0 + i*dy
            if (
                abs(x - x0) > half_width0 and
                abs(x - x1) > half_width1
            ) or (
                abs(y - y0) > half_height0 and
                abs(y - y1) > half_height1
            ): c.set(x, y)
        label = ''
        if e.show_label:
            label += e.label
        if e.show_att:
            for key in n.att:
                label += ', %s: %s'%(key, str(n.att[key]))
        c.set_text(x0 + (l // 2)*dx, y0 + (l // 2)*dy, label)

    def draw(self):
        """Draw the graph
        """
        c = Canvas()
        for node in self.nodes.itervalues():
            self.draw_node(c, node)
        for edge in self.edges:
            self.draw_edge(c, edge)
        print(c.frame())
