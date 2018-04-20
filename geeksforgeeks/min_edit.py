# https://www.youtube.com/watch?v=We3YDTzNXEk

# minimum edits to go from s2 to s1
def min_edit(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0] * n for i in range(m)]

    # base case
    for i in range(n):
        dp[0][i] = i

    for i in range(m):
        dp[i][0] = i

    for i in range(1, m):
        for j in range(1, n):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1]+1, dp[i-1][j-1] + 1)

    return dp[m-1][n-1]

assert(min_edit("abcab", "abc") == 2)
assert(min_edit("aaaa", "aadd") == 2)
assert(min_edit("abcd", "a") == 3)
print("passed")
