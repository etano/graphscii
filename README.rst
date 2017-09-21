graphscii
=========

Print ASCII graphs in the terminal.

.. image:: https://github.com/etano/graphscii/blob/master/examples/risk.png
    :alt: Risk graph
    :width: 100%
    :align: center

Installation
------------

The easiest way to install is with pip::

    sudo pip install graphscii

To manually install, use::

    sudo python ./setup.py install

Usage
-----

To draw a graph, create a Graph object, add nodes and edges, and invoke the `draw()` method::

    from graphscii import Graph

    g = Graph()
    g.add_node('n0', pos=[0.1, 0.1])
    g.add_node('n1', pos=[0.9, 0.1])
    g.add_node('n2', pos=[0.5, 0.9])
    g.add_edge('n0', 'n1', label='e0')
    g.add_edge('n1', 'n2', label='e1')
    g.add_edge('n2', 'n0', label='e2')
    g.draw()

.. image:: https://github.com/etano/graphscii/blob/master/examples/simple.png
    :alt: Simple triangle graph
    :width: 50%
    :align: center

For more examples, see the `examples` directory.
