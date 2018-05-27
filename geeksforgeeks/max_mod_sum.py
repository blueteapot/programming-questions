def max_mod_sum(lst, m):
    n = len(lst)
    suffix_sum = [-1] * n
    suffix_sum[0] = 0

    suffix_sum[0] = lst[0] % m
    for i in range(1, n):
        suffix_sum[i] = (suffix_sum[i - 1] + lst[i]) % m

    


# test
print(max_mod_sum([3,2,7,4], 7))
