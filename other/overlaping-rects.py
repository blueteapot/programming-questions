def overlapped_area(r0, r1):
    # width calculation

    w = min(r0[1][0], r1[1][0]) - max(r0[0][0], r1[0][0])
    if w < 0:
        return 0

    h = min(r0[1][1], r1[1][1]) - max(r0[0][1], r1[0][1])
    if h < 0:
        return 0

    return w * h

assert(overlapped_area([(2, 1), (5, 5)], [(3, 2), (5, 7)]) == 6)
assert(overlapped_area([(1, 1), (2, 2)], [(3, 3), (4, 4)]) == 0)
print("success!")
