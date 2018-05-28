class Node:
    def __init__(self, v):
        self.v = v
        self.next = None

    def set_next(node):
        self.next = node


def swap_alternate(head):

    if head is None:
        return

    new_head = None
    prev = head
    current = head.next

    while current != None and current.next != None:
        prev.next = current.next.next
        current.next = current



# test
head = Node(0)
current = head
for i in range(1, 10):
    node = Node(i)
    current.next = node
    current = node

new_head = swap_alternate(head)
