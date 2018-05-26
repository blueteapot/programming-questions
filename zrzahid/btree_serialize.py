class Node:
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None

    def add_right(self, r):
        self.r = r

    def add_left(self, l):
        self.l = l


def print_btree(root):
    if root is not None:
        print(root.v)
        print_btree(root.l)
        print_btree(root.r)


def btree_serialize(root, lst):

    if root is None:
        return lst

    lst.append(root.v)
    btree_serialize(root.l, lst)
    btree_serialize(root.r, lst)

    return lst


def btree_deserialize(lst):
    if len(lst) == 0:
        return None

    pop = lst.pop(0)
    node = Node(pop)
    l_node = btree_deserialize(lst)
    r_node = btree_deserialize(lst)
    node.l = l_node
    node.r = r_node

    return node


btree = btree_deserialize([1, 2, None, None, 3, 4, 5])
print(btree_serialize(btree, []))
