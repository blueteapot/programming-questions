def first_occur(lst, left, right, v):

    if left == right:
        return left if lst[left] == v else None

    mid = (left + right) // 2
    if lst[mid] < v:
        return first_occur(lst, mid + 1, right, v)
    elif lst[mid] > v:
        return first_occur(lst, left, mid - 1, v)
    else:
        # lst[mid] == v
        return first_occur(lst, left, mid, v)

# test
lst = [1, 1, 1, 2, 2, 3, 3, 3, 4]
n = len(lst)
assert(first_occur(lst, 0, n - 1,  2) == 3)
assert(first_occur(lst, 0, n - 1,  1) == 0)
assert(first_occur(lst, 0, n - 1,  4) == n - 1)
assert(first_occur(lst, 0, n - 1,  3) == 5)
print("success")
