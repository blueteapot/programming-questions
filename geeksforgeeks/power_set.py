import itertools

def power_set_rec(lst, bools, i):
    if i == len(lst):
        print(list(itertools.compress(lst, bools)))
    else:
        bools[i] = False
        power_set_rec(lst, bools, i + 1)
        bools[i] = True
        power_set_rec(lst, bools, i + 1)




# test
power_set_rec([1,2,3,4], [0, 0, 0, 0], 0)
