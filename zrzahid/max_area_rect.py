def max_area_rect(lst):
    n = len(lst)
    right = [-1] * n
    left = [-1] * n

    right[n - 1] = n
    for i in range(n - 2, -1, -1):
        right[i] = i + 1 if lst[i] > lst[i + 1] else right[i + 1]

    left[0] = -1
    for i in range(1, n):
        left[i] = i - 1 if lst[i - 1] < lst[i] else left[i - 1]

    # print(lst)
    # print(left)
    # print(list(range(0, n)))

    max_res = -1
    for i in range(n):
        right_len = right[i] - i -1
        left_len = i - left[i] + 1
        h = min(lst[right_len - 1], lst[left_len + 1])
        res = (right_len + left_len) * h
        if res > max_res:
            max_res = res
            print(i, left[i], right[i])

    return max_res





# test
print(max_area_rect([4, 2, 1, 8, 6, 8, 5, 2])) # expected result: 20
