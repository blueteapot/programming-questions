def min_in_rotated(lst):

    print(lst)

    n = len(lst)
    left = 0
    right = n - 1
    mid  = n // 2

    if n == 1:
        return lst[0]

    if n == 2:
        return lst[0] if lst[0] < lst[1] else lst[1]

    print("mid = ", lst[mid])
    if lst[mid] < lst[mid - 1] and lst[mid] < lst[mid + 1]:
        return lst[mid]
    if lst[mid] < lst[left]:
        return min_in_rotated(lst[left:mid])
    return min_in_rotated(lst[mid:right + 1])


# test
print(min_in_rotated([5,6,7,8,9,1,2,3,4]))
