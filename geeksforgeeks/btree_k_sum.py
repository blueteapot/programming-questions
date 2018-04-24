class Node:
    def __init__(self, v):
        self.v = v
        self.r = None
        self.l = None

    def add_right(self, node):
        self.r = node

    def add_left(self, node):
        self.l = node

def k_level_sum(root, k):
    if root is None:
        return 0

    if k == 0:
        return root.v

    return k_level_sum(root.l, k - 1) + k_level_sum(root.r, k - 1)


# test
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.l = n2
n1.r = n3

n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

n2.l = n6
n3.l = n4
n3.r = n5

assert(k_level_sum(n1, 2) == 15)
assert(k_level_sum(n1, 1) == 5)
assert(k_level_sum(n1, 0) == 1)
print("passed")
