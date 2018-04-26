class Stack:
    def __init__(self):
        self.s = []

    def push(self, v):
        self.s.append(0, v)

    def pop(self):
        if len(self.s) == 0:
            return None
        return self.s.pop(0)

    def top(self):
        if self.s == 0:
            return None
        return self.s[0]

    def is_empty(self):
        return len(self.s) == 0

def stack_sort_rec(stack):
    if not stack.is_empty():
        item = stack.pop()
