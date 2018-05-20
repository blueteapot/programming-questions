def smallest_two(lst):
    n = len(lst)
    s1 = float('inf')
    s2 = float('inf')

    for i in range(n):
        if lst[i] < s1:
            s2 = s1
            s1 = lst[i]
        elif lst[i] < s2:
            s2 = lst[i]

    return (s1, s2)


# test
assert(smallest_two([2,4,6,8,10,3,5,7,9]) == (2,3))
print("success")
