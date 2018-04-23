def queries_on_mat(mat, queries):
    for i in range(len(queries)):
        query = queries[i]
        top_left = query[0]
        bottom_right = query[1]

        for i in range(top_left[0], bottom_right[0] + 1):
            for j in range(top_left[1], bottom_right[1] + 1):
                mat[i][j] += 1

# test
N = 6
mat = [ [0] * N for _ in range(N)]
queries = [((1, 2), (4, 5))]
queries_on_mat(mat, queries)
