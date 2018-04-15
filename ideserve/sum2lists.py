def helper(lst1, lst2, carry):
    if len(lst1) == 0 and len(lst2) == 0:
        if carry == 0:
            return []
        else:
            return [carry]

    v1 = 0 if len(lst1) == 0 else lst1.pop()
    v2 = 0 if len(lst2) == 0 else lst2.pop()

    v = v1 + v2 + carry
    carry = 1 if v >= 10 else 0
    v = v if v < 10 else v % 10

    return helper(lst1, lst2, carry) + [v]

def sum2lists(lst1, lst2):
    return helper(lst1, lst2, 0)

assert(sum2lists([1, 2], [1, 9]) == [3, 1])
assert(sum2lists([5, 0], [7, 0]) == [1,2,0])
print("passed")
