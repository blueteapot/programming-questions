class BinaryHeap:
    def __init__(self, depth):
        self.size = 0
        self.heap = [None] * 2**depth
        self.capacity = 2**depth

    def up_heap(self, pos):

        if pos == 0:
            return self.heap[pos]

        if self.heap[int(pos / 2)] == None or self.heap[pos] > self.heap[int(pos / 2)]:
            self.heap[pos], self.heap[int(pos / 2)] = self.heap[int(pos / 2)], self.heap[pos]
            self.up_heap(int(pos / 2))

    def insert(self, v):
        if self.size == self.capacity:
            return None
        self.heap[self.capacity - 1] = v
        return self.up_heap(self.capacity - 1)

    def parent(self, i):
        return self.heap(int(i / 2))

    def left_child(i):
        return self.heap(2 * i + 1)

    def right_child(i):
        return self.heap(2 * i + 2)


# test
bheap = BinaryHeap(4)
for i in range(16):
    bheap.insert(i)

print(bheap.heap)
