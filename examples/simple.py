from graphscii import Graph

g = Graph()
g.add_node('n0', pos=[0.1, 0.1])
g.add_node('n1', pos=[0.3, 0.1])
g.add_node('n2', pos=[0.2, 0.3])
g.add_edge('n0', 'n1', label='e0')
g.add_edge('n1', 'n2', label='e1')
g.add_edge('n2', 'n0', label='e2')
g.draw()
