class Node:
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None

    def add_right(self, r):
        self.r = r

    def add_left(self, l):
        self.l = l


def bt_to_dll(root):

    if root == None:
        return None

    if root.l is not None:

        head = bt_to_dll(root.l)
        right_most = head

        while right_most is not None:
            right_most = right_most.r

        right_most.r = root
        root.l = right_most

    if root.r is not None:

        head = bt_to_dll(root.r)
        left_most = head

        while left_most is not None:
            left_most = left_most.l

        root.r = left_most
        left_most.l = root

# test
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.l = n2
n1.r = n3

l_head, _ = bt_to_dll(n1)
current = l_head
while current is not None:
    print(current.v)
    current = current.r
