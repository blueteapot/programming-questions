class Node:
    def __init__(self, v):
        self.v = v
        self.r = None
        self.l = None

    def add_right(self, node):
        self.r = node

    def add_left(self, node):
        self.l = node

def lca(root, n1, n2):

    if root is None:
        return None

    if n1 is root or n2 is root:
        return root

    left_lca = lca(root.l, n1, n2)
    right_lca = lca(root.r, n1, n2)

    if left_lca is not None and right_lca is not None:
        return root

    if left_lca is None:
        return right_lca
    return left_lca
