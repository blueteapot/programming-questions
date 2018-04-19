def reverse_queue(q):
    if len(q) == 1:
        return q

    rear = q.pop(0)
    q = reverse_queue(q)
    q.append(rear)
    return q

# test
q = [1,2,3,4,5]
print(reverse_queue(q))
