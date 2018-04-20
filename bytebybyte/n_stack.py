class NStack:
    def __init__(self, n, size):
        self.size = size
        self.n = n
        self.lst = [None] * (size * n)
        self.idx = [0] * n
        for i in range(n):
            self.idx[i] = i * n

        print(self.idx)

    def push(self, v, i):
        if self.idx[i] == (i + 1) * self.size:
            print("Stack is full")
        else:
            self.lst[self.idx[i]] = v
            self.idx[i] += 1

    def pop(self, i):
        if self.idx[i] == i * self.size:
            print("Stack is empty")
            return None
        self.idx[i] -= 1
        v = self.lst[self.idx[i]]
        self.lst[self.idx[i]] = None
        return v

    def __str__(self):
        return str(self.lst)

# test
nstack = NStack(n=5, size=5)
for i in range(5):
    for j in range(5):
        nstack.push(j, i)

print(nstack)
