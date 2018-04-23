def unbounded_ks(W, vs, ws):

    n = len(vs)

    # dp[i] = max value using all items
    # base case is dp[0] = 0
    dp = [0] * (W + 1)

    for i in range(W+1):
        for j in range(n):
            if ws[j] <= i:
                dp[i] = max(dp[i], dp[i - ws[j]] + vs[j])

    return dp[W]

# test
W = 10
vs = [1, 2, 6, 7]
ws = [1, 3, 4, 5]

assert(unbounded_ks(W, vs, ws) == 14)
print("passed")
