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

    def __init__(
        self, label, att={}, pos=[0, 0], shape=[10, 10], show_label=True, show_att=False
    ):
        """Initialize Node class

           Args:
               label (str): Label for the node
               att (dict(str, val)): Dictionary of attributes for the node
               pos (list(float)): x, y position between 0 and 1
               shape (list(float)): Shape of node
               show_label (bool): Whether or not to show the label
               show_att (bool): Whether or not to show the attributes
        """
        if len(pos) != 2:
            raise ValueError("pos must be of length 2")
        if pos[0] < 0 or pos[0] > 1:
            raise ValueError("x position must be between 0 and 1")
        if pos[1] < 0 or pos[1] > 1:
            raise ValueError("y position must be between 0 and 1")
        if len(shape) != 2:
            raise ValueError("shape must be of length 2")
        self.label = label
        self.att = dict(att)
        self.pos = list(pos)
        self.shape = list(shape)
        self.show_label = show_label
        self.show_att = show_att
