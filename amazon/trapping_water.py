# https://www.geeksforgeeks.org/trapping-rain-water/

def trapping_water(lst):
    print(lst)
    n = len(lst)
    left_highest = [-1] * n
    right_highest = [-1] * n

    left_highest[0] = -1
    left_highest[1] = lst[0]

    for i in range(2, n):
        left_highest[i] = max(lst[i], left_highest[i - 1])

    print("L:", right_highest)

    right_highest[n - 1] = -1
    right_highest[n - 2] = lst[n - 1]

    for i in range(n - 3, -1, -1):
        right_highest[i] = max(lst[i], right_highest[i + 1])


    print("R:", right_highest)

    total_water = 0
    for i in range(1, n - 1):
        total_water += min(right_highest[i], left_highest[i]) - lst[i]


    return total_water


# test
print(trapping_water([3,0,0,2,0,4]))
