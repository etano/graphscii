from __future__ import print_function
from drawille import Canvas
from math import sqrt, atan, cos, sin, pi

c = Canvas()

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

    def draw(self):
        for i in range(self.width):
            c.set(self.x0 + i, self.y0)
            c.set(self.x0 + i, self.y0 + self.height)
        for i in range(self.height):
            c.set(self.x0, self.y0 + i)
            c.set(self.x0 + self.width, self.y0 + i)
        c.set_text(self.x0 + (self.width // 2), self.y0 + (self.height // 2), self.label)

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

    def draw(self):
        #  (n0)
        #     .
        #      .
        #      (n1)
        x0 = self.n0.x0 + (self.n0.width // 2)
        x1 = self.n1.x0 + (self.n1.width // 2)
        y0 = self.n0.y0 + (self.n0.height // 2)
        y1 = self.n1.y0 + (self.n1.height // 2)
        x_sign = 1 if x1 > x0 else -1
        y_sign = 1 if y1 > y0 else -1
        width = abs(x1-x0)
        height = abs(y1-y0)
        l = sqrt(width**2 + height**2)
        theta = 0.5*pi if not height else atan(float(width) / float(height))
        for i in range(int(l)):
            x = x0 + i*sin(theta)*x_sign
            y = y0 + i*cos(theta)*y_sign
            if (
                abs(x-x0) > (self.n0.width // 2) and
                abs(x-x1) > (self.n1.width // 2)
            ) or (
                abs(y-y0) > (self.n0.height // 2) and
                abs(y-y1) > (self.n1.height // 2)
            ): c.set(x, y)
            if i == l // 2:
                c.set_text(x, y, self.label)


n0 = Node(0, 20, 10, 10, 'n0')
n0.draw()
n1 = Node(20, 20, 10, 10, 'n1')
n1.draw()
n2 = Node(25, 0, 10, 10, 'n2')
n2.draw()
e = Edge(n0, n2, 'e0')
e.draw()
e = Edge(n2, n1, 'e1')
e.draw()
e = Edge(n1, n0, 'e2')
e.draw()
print(c.frame())
