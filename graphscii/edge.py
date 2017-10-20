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
