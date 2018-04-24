class Node:
    def __init__(self, v, left=None, right=None):
        self.v = v
        self.left = left
        self.right = right

def convert_to_sum_property(root):
    if root == None:
        return None

    node_data = root.v
    right_data = 0 if root.right is None else root.right.v
    left_data = 0 if root.left is None else root.left.v

    children_sum = right_data + left_data

    # TODO: complete this function.
