## http://www.zrzahid.com/search-in-a-2d-array-or-matrix/
##
def mat_search_v2(mat, v):
    n = len(mat)
    row = 0
    col = n - 1

    while row < n and col >= 0:
        if mat[row][col] == v:
            return (row, col)
        if mat[row][col] < v:
            row += 1
        else:
            col -= 1

    return (-1, -1)

# test
mat = [
[1,4,7],
[2,5,8],
[3,6,9]
]

assert(mat_search_v2(mat, 6) == (2, 1))
assert(mat_search_v2(mat, 2) == (1, 0))
assert(mat_search_v2(mat, 0) == (-1, -1))
assert(mat_search_v2(mat, 10) == (-1, -1))

print("success")
