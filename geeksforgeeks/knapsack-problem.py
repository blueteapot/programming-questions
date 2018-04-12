# https://www.geeksforgeeks.org/knapsack-problem/

maxw = 50
ws = [10, 20, 30]
vs = [60, 100, 120]

# (1) naive solution
def knapsack_naive(ws, vs, maxw):

    if len(ws) == 0 or maxw == 0:
        return 0

    w = ws.pop()
    v = vs.pop()

    if w > maxw:
        return knapsack_naive(ws, vs, maxw)
    return max(v + knapsack_naive(ws, vs, maxw - w), knapsack_naive(ws, vs, maxw))

# (2) DP solution, O(nW)
def knapsack_dynamic(ws, vs, W):
    n = len(ws)
    K = [[0] * (W+1) for i in range(n+1)]

    for i in range(n+1):
        for w in range(W+1):

            if i  == 0 or w == 0: # knapsack is empty or no more weight to carry
                K[i][w] = 0
            else:
                if ws[i-1] > w:
                    K[i][w] = K[i-1][w]
                else:
                    K[i][w] = max(vs[i-1] + K[i-1][w-ws[i-1]], K[i-1][w])
    return K[n][W]

print(knapsack_dynamic(ws, vs, maxw)) # should print 220
