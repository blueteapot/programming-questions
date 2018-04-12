# https://www.geeksforgeeks.org/knapsack-problem/

maxw = 50
ws = [10, 20, 30]
vs = [60, 100, 120]

# (1) naive solution
def knapsack_rec(ws, vs, maxw):

    if len(ws) == 0 or maxw == 0:
        return 0

    w = ws.pop()
    v = vs.pop()

    if w > maxw:
        return knapsack_rec(ws, vs, maxw)
    return max(v + knapsack_rec(ws, vs, maxw - w), knapsack_rec(ws, vs, maxw))

print(knapsack_rec(ws, vs, maxw)) # should print 220
