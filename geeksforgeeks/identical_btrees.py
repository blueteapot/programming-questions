class Node:
    def __init__(self, v):
        self.v = v
        self.r = None
        self.l = None

    def add_right(self, node):
        self.r = node

    def add_left(self, node):
        self.l = node

def identical_btrees(root1, root2):
    if root1 is None and root2 is None:
        return True
    if (root1 is not None and root2 is None) or (root2 is not None and root1 is None):
        return False

    if root1.v != root2.v:
        return False

    return identical_btrees(root1.l, root2.l) and identical_btrees(root1.r, root2.r)

# test
n1 = Node(1)
n2 = Node(2)
n1.add_left(n2)
n3 = Node(3)
n2.add_right(n3)

m1 = Node(1)
m2 = Node(2)
m1.add_left(m2)
m3 = Node(3)
m2.add_right(m3)

assert(identical_btrees(n1, m1) == True)
print("passed")
