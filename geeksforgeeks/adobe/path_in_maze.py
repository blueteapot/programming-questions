import numpy as np


def path(maze, start, end, n):

    d = [[float('inf')] * n for i in range(n)]
    visited = [[0] * n for i in range(n)]
    d[start[0]][start[1]] = 0
    visited[start[0]][start[1]] = 1
    p = [[None] * n for i in range(n)]

    stack = [start]

    while len(stack) > 0:

        square = stack.pop(0)
        x = square[0]
        y = square[1]
        visited[x][y] = 1

        if x == end[0] and y == end[1]:
            break

        if x > 0:
            if maze[x-1][y] == 0 and d[x-1][y] > d[x][y] + 1:
                d[x - 1][y] = d[x][y] + 1
                p[x - 1][y] = (x, y)
            if maze[x-1][y] == 0  and visited[x-1][y] == 0:
                stack.insert(0, (x-1, y))

        if x < n - 1:
            if maze[x + 1][y] == 0 and d[x + 1][y] > d[x][y] + 1:
                d[x + 1][y] = d[x][y] + 1
                p[x + 1][y] = (x, y)
            if maze[x + 1][y] == 0 and visited[x+1][y] == 0:
                stack.insert(0, (x+1, y))

        if y > 0:
            if maze[x][y - 1] == 0 and d[x][y - 1] > d[x][y] + 1:
                d[x][y - 1] = d[x][y] + 1
                p[x][y - 1] = (x, y)
            if maze[x][y - 1] == 0 and visited[x][y - 1] == 0:
                stack.insert(0, (x, y - 1))

        if y < n - 1:
            if maze[x][y + 1] == 0 and d[x][y + 1] > d[x][y] + 1:
                d[x][y + 1] = d[x][y] + 1
                p[x][y + 1] = (x, y)
            if maze[x][y + 1] == 0  and visited[x][y + 1] == 0:
                stack.insert(0, (x, y + 1))

    d_pretty = np.array(d)
    print(d_pretty)

    p_pretty = np.array(p)
    print(p_pretty)


    current = p[end[0]][end[1]]
    while current is not None:
        print(current)
        current = p[current[0]][current[1]]


maze = [
[0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 0],
[0, 0, 0, 1, 0, 0],
[0, 0, 0, 1, 0, 0],
[0, 0, 0, 1, 0, 0],
[0, 0, 0, 1, 0, 0]
]
# test
path(maze, (5, 2), (5, 5), 6)
