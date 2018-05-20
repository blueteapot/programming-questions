class Node:
    def __init__(self, v):
        self.v = v
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node

    def to_str(self):
        s = str(self.v)
        current = self
        while current.get_next() != None:
            current = current.get_next()
            s += " -> " + str(current.v)
        print(s)

def reverse_k(start, k, before):
    prev = start
    current = start.get_next()
    i = 1

    while i < k:
        next = current.get_next()
        current.set_next(prev)
        prev = current
        current = next
        i += 1

    if before is not None:
        before.set_next(prev)
    return prev

def reverse_every_k(head, k, n):
    m = n // k
    before = None
    for i in range(m):
        head = reverse_k(head, k, before)
        print("head.v =", head.v)
        before = head


head = Node(0)
current = head
for i in range(1, 10):
    current.set_next(Node(i))
    current = current.get_next()

head.to_str()
reverse_every_k(head, 3, 10).to_str()
