class Node:
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None

    def add_right(self, r):
        self.r = r

    def add_left(self, l):
        self.l = l


def double_tree(root):

    if root is None:
        return

    temp = root.v

    # leaf
    if root.l == None and root.r == None:
        root.l = Node(root.v)
        return


    if root.l is not None:
        original_l = root.l
        root.l = Node(root.v)
        root.l.v = root.v
        root.l.l = original_l

    double_tree(root.r)
    double_tree(root.l.l)


def print_tree(root, depth):
    if root == None:
        return
    s = ' ' * depth + str(root.v)
    print(s)
    print_tree(root.l, depth + 1)
    print_tree(root.r, depth + 1)


# test
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.l = n2
n1.r = n3

print("before")
print_tree(n1, 0)
double_tree(n1)
print("after:")
print_tree(n1, 0)
