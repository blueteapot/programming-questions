def walkable(mat, i, j):
    if i < 0 or j < 0 or i >= len(mat) or j >= len(mat[0]):
        return False
    return True

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def walk(mat, dp, i, j):

    if dp[i][j] > 0:
        return dp[i][j]

    max_len = 1
    for dir in dirs:
        next_i = i + dir[0]
        next_j = j + dir[1]
        if walkable(mat, next_i, next_j) and mat[i][j] < mat[next_i][next_j]:
            len = 1 + walk(mat, dp, next_i, next_j)
            if len > max_len:
                max_len = len

    dp[i][j] = max_len
    return dp[i][j]


def longest_inc_path(mat, dp):
    n = len(mat)
    for i in range(n):
        for j in range(n):
            walk(mat, dp, i, j)

    print(dp)


# test
n = 3
mat = [[3,4,5], [3,2,6], [2,2,1]]
dp = [[0] * n for i in range(n)]

longest_inc_path(mat, dp)
