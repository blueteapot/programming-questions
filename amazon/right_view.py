# https://www.geeksforgeeks.org/right-view-binary-tree-using-queue/
#
class Node:
    def __init__(self, v):
        self.v = v
        self.r = None
        self.l = None

    def add_right(self, node):
        self.r = node

    def add_left(self, node):
        self.l = node

def right_view(root):
    q = []
    q.append(root)
    level = 1
    count = 0

    while len(q) > 0:
        level_size = len(q)
        count = 0
        while count < level_size:
            node = q.pop(0)

            if node.l is not None:
                q.append(node.l)
            if node.r is not None:
                q.append(node.r)

            count += 1

        print(node.v)

# test
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.l = n2
n1.r = n3

n4 = Node(4)
n5 = Node(5)

n2.l = n4
n2.r = n5

n6 = Node(6)
n3.l = n6

n7 = Node(7)
n6.r = n7

right_view(n1)
