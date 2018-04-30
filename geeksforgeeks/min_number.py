# https://www.geeksforgeeks.org/form-minimum-number-from-given-sequence/

def min_number(seq):
    stack = []
    for i in range(1, 10):
        stack.insert(0, i)

    n = len(seq)
    current = seq[0]
    i = 0
    while current == seq[i]:






# test
assert(min_number("IIDDD") == 126543)
