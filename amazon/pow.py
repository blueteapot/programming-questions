def pow_rec(x, y):
    """
    returns x^y
    """

    if y == 0:
        return 1

    res = pow_rec(x, y // 2)
    res_squared = res * res
    if y % 2 == 0:
        return res_squared
    else:
        return x * res_squared


# test
assert(pow_rec(2, 8) == 256)
assert(pow_rec(2, 9) == 512)
print("success")
