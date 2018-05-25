def peek_elem(lst):
    n = len(lst)
    if n == 1:
        return lst[0]
    if n == 2:
        return lst[0] if lst[0] >= lst[1] else lst[1]

    mid = len(lst) // 2
    if lst[mid] >= lst[mid -1] and lst[mid] >= lst[mid + 1]:
        return lst[mid]
    elif lst[mid - 1] >= lst[mid - 1]:
        return peek_elem(lst[0:mid])
    else:
        return peek_elem(lst[mid:])

# test
assert(peek_elem([100, 80, 60, 50, 20]) == 100)
assert(peek_elem([5, 10, 20, 15]) == 20)
print("success")
