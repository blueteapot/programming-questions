from math import ceil

def min_pal_partition(s):
    n = len(s)
    dp = [[float('inf')] * n for i in range(n)]

    for i in range(n):
        for j in range(n - i):
            x = j
            y = i + j
            print(x, y)
            if x == y or is_palindrom(s, x, y):
                dp[x][y] = 0
            else:
                for k in range(y - x):
                    res = dp[x][k] + dp[k + 1][y] + 1
                    if res < dp[x][y]:
                        dp[x][y] = res

    return dp[0][n-1]

def is_palindrom(s, x, y):
    n = int(ceil((y - x) / 2))
    for i in range(n):
        if s[x + i] != s[y - i]:
            return False
    return True

# test is_palindrom
assert(is_palindrom("abc", 0, 2) == False)
assert(is_palindrom("aba", 0, 2) == True)
assert(is_palindrom("1234aba5678", 4, 6) == True)

# test min_pal_partition
print(min_pal_partition("abcdc"))
