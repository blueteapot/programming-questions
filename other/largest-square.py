def largest_1s_square(mat):
    n = len(mat)
    m = len(mat[0])
    result = 0
    a = [[0] * m for i in range(n)]

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                continue
            if i == 0 or j == 0:
                a[i][j] = mat[i][j]
            else:
                a[i][j] = 1 + min(a[i-1][j], a[i][j-1], a[i-1][j-1])

            if result < a[i][j]:
                result = a[i][j]

    return result

# test
mat = [[1,1,0,1,0], [0,1,1,1,0], [1,1,1,1,0], [0,1,1,1,1]]
assert(largest_1s_square(mat) == 3)
print("passed")
