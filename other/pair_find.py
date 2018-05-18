def pair_find(lst, s):
    left = 0
    right = len(lst) - 1

    while left < right:
        print(left, right)
        if lst[left] + lst[right] == s:
            return (left, right)
        elif lst[left] + lst[right] > s:
            right -= 1
        else:
            left += 1

    return None
