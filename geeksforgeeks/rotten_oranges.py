# 0 - empty
# 1 - fresh
# 2 - rotten
# 3 - affected


# _ _ _ _
# _ _ x _
# _ _ _ _
# _ _ _ _
# _ _ _ _

def is_all_rotten(mat, n, m):

    # push all rotten oranges to a queue
    rotten_q = []
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 2:
                rotten_q.append((i, j))


    while len(rotten_q) > 0:

        rotten = rotten_q.pop()
        path_q = [rotten]

        while len(path_q) > 0:
            orange = path_q.pop()
            x = orange[0]
            y = orange[1]
            if mat[x][y] == 3:
                continue

            mat[x][y] = 3

            if x > 0:
                if mat[x - 1][y] != 3 and mat[x - 1][y] != 0:
                    path_q.append((x - 1, y))
            if x < n - 1:
                if mat[x + 1][y] != 3 and mat[x + 1][y] != 0:
                    path_q.append((x + 1, y))
            if y > 0:
                if mat[x][y-1] != 3 and mat[x][y-1] != 0:
                    path_q.append((x, y - 1))
            if y < m - 1:
                if mat[x][y + 1] != 3 and mat[x][y + 1] != 0:
                    path_q.append((x, y + 1))

        print(mat)
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    return False
        return True

# test
mat = [
[1, 0, 0, 0],
[1, 1, 1, 1],
[0, 1, 0, 0],
[0, 2, 0, 0]
]


assert(is_all_rotten(mat, 4, 4) == True)
print("pass")
