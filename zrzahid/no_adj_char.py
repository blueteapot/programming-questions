def no_adj_char(lst):
    n = len(lst)
    dict = {}
    for i in range(n):
        if lst[i] in dict:
            dict[lst[i]] += 1
        else:
            dict[lst[i]] = 1

    for item in sorted(dict.items()):
        print(item)


# test
no_adj_char([1,2,3,1,1,1,3,2,4])
