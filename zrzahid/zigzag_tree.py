class Node:
    def __init__(self, v):
        self.v = v
        self.r = None
        self.l = None

    def add_right(self, node):
        self.r = node

    def add_left(self, node):
        self.l = node

def zigzag(tree, priority_dict, current_priority):

    if tree is None:
        return

    if current_priority in priority_dict:
        priority_dict[current_priority].append(tree.v)
    else:
        priority_dict[current_priority] = [tree.v]

    zigzag(tree.l, priority_dict, current_priority - 1)
    zigzag(tree.r, priority_dict, current_priority + 1)


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

priority_dict = {}
zigzag(n1, priority_dict,  0)
print(priority_dict)
