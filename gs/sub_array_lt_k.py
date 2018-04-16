from numpy import prod


def subarray_lt_k(arr, k):
    n = len(arr)
    l = 0
    r = 0
    p = 1
    count = 0

    while r < n:
        p *= arr[r]

        # find the smallest l so l * ... * r < k
        while l < r and p >= k:
            p /= arr[l]
            l += 1

        if p < k:
            count += r - l + 1

        r += 1

    return count

assert(subarray_lt_k([1,2,3,4], 10) == 7)
print("passed")
