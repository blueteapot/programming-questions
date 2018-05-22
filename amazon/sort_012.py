def sort_012(lst):
    n = len(lst)
    low = 0
    mid = 0
    high = n - 1

    while mid <= high:
        if lst[mid] == 0:
            lst[low], lst[mid] = lst[mid], lst[low]
            low += 1
            mid += 1
            
        elif lst[mid] == 1:
            mid += 1

        else:
            # lst[mid] == 2
            lst[mid], lst[high] = lst[high], lst[mid]
            high -=1

    print(lst)

# test
sort_012([1,0,2,2,0,1,1,0,2,1,0])
