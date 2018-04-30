def search(arr):
    pass # todo

def find_pivot(arr):
    return find_pivot_helper(arr, 0, len(arr) - 1)

def find_pivot_helper(arr, low, high):

    if high < low:
        return -1

    if high == low:
        return low

    mid = (low + high) // 2
    if arr[mid] > arr[mid + 1]:
        return mid

    if arr[mid] < arr[mid - 1]:
        return mid - 1

    if arr[mid] > arr[high]:
        return find_pivot(arr, mid + 1, high)
    return find_pivot(arr, low, mid - 1)


# test
print(find_pivot([4, 5, 6, 7, 1, 2, 3]))
