def sum2zero(lst):
    lst.sort()
    print(lst)
    l = 0
    r = len(lst) - 1

    while l <= r:
        print(l, r)
        sum = lst[l] + lst[r]
        if sum == 0:
            return lst[l], lst[r]
        if sum > 0:
            r -= 1
        else:
            l += 1

print(sum2zero([3,6,2, -2]))
