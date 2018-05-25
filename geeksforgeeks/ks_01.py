## revisting the KS problem:
## https://www.geeksforgeeks.org/knapsack-problem/
##
def ks_01(ws, vs, w, n):

    if n == 0 or w == 0:
        return 0

    w_n = ws[n - 1]
    if  w_n > w:
        return ks_01(ws, vs, w, n - 1)
    return vs[n - 1] + max(ks_01(ws, vs, w - w_n, n - 1), ks_01(ws, vs, w - w_n, n - 1))


# test
n = 3
w = 50
vs = [60, 100, 120]
ws = [10, 20, 30]

print(ks_01(ws, vs, w, n))
