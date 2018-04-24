
def min_chain_mul(ps):
    n = len(ps) - 1
    dp = [[float('inf')] * n for i in range(n)]
    for i in range(n):
        dp[i][i] = 0

    for i in range(1, n):
        for j in range(n-i, 0, -1):
            for k in range(1, i):
                res = dp[i][k] + dp[k][j] + ps[i] * ps[k] * ps[j]
                print("res = ", res)
                if res < dp[i][j]:
                    dp[i][j] = res

    print(dp)

# test
min_chain_mul([10, 20, 30, 40, 50])
