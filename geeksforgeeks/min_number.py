# https://www.geeksforgeeks.org/form-minimum-number-from-given-sequence/

def min_number(seq):
    stack = []
    for i in range(1, 10):
        stack.insert(0, i)

    n = len(seq)
    for i in range(n):
        



# test
assert(min_number("IIDDD") == 126543)
