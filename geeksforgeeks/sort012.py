#
# 00000(L)11111(M)?????H2222222

def sort_012(lst):
    n = len(lst)
    l = 0
    m = 0
    h = n - 1


    while m <= h:
        if lst[m] == 0:
            lst[l], lst[m] = lst[m], lst[l]
            l += 1
            m += 1
        elif lst[m] == 1:
            m += 1
        else: # lst[l] == 2
            lst[m], lst[h] = lst[h], lst[m]
            h -= 1

    return lst

# test
print(sort_012([2,1,2,0,0,1,1,1,2,2,1,0]))
