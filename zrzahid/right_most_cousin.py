## http://www.zrzahid.com/find-the-rightmost-cousin-of-a-binary-tree/
## TODO: check if there's no such cousin (minor code change)
##
class Node:
    def __init__(self, v):
        self.v = v
        self.r = None
        self.l = None

    def add_right(self, node):
        self.r = node

    def add_left(self, node):
        self.l = node

def find_level_helper(root, v, k):

    if root == None:
        return None

    if root.v == v:
        return k

    ret_k = find_level_helper(root.r, v, k + 1)
    if ret_k != None:
        return ret_k

    ret_k = find_level_helper(root.l, v, k + 1)
    if ret_k != None:
        return ret_k

    return None


def find_level(root, v):
    return find_level_helper(root, v, 0)


def right_most_cousin_helper(root, v, h):
    if h == 0:
        return root.v

    if root.r is not None:
        ret_node = right_most_cousin_helper(root.r, v, h - 1)
        if ret_node is not None:
            return ret_node

    if root.l is not None:
        ret_node = right_most_cousin_helper(root.l, v, h - 1)
        if ret_node is not None:
            return ret_node

    return None


def right_most_cousin(root, v):
    h = find_level(root, v)
    if h is None:
        return None
    return right_most_cousin_helper(root, v, h)


# test
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.l = n2
n1.r = n3

n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

n3.r = n6
n2.l = n4
n2.r = n5

assert(right_most_cousin(n1, 4) == 6)
assert(right_most_cousin(n1, 2) == 3)
assert(right_most_cousin(n1, 5) == 6)
print("success")
