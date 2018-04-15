inbox = []
outbox = []

def enqueue(item):
    inbox.insert(0, item)

def dequeue():
    if not outbox and not inbox:
        return None

    if not outbox:
        while len(inbox) > 0:
            outbox.insert(0, (inbox.pop(0)))
    return outbox.pop(0)

res = []
enqueue(1)
enqueue(2)
res.append(dequeue())
enqueue(3)
res.append(dequeue())
enqueue(4)
res.append(dequeue())
res.append(dequeue())

assert(res == [1,2,3,4])
print("passed")
