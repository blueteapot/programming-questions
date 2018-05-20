## (A, 1), (B, 2), (C, 3), (D, 4), (E, 5),
## (F, 6), (G, 7), (H, 8), (I, 9), (J, 10),
#  ..., (Z, 26)
def count_dec(code):
    n = len(code)
    count = [0] * (n + 1)
    count[0] = 1
    count[1] = 1

    for i in range(2, n):
        if code[i] == '0':
            count[i] = count[i - 2]
        else:
            # current digit is not '0'
            if code[i - 1] == '1' or (code [i - 1] == '2' and code[i] < '7'):
                # last two digits can form a valid number but also
                # can be seen as two different characters.
                count[i] = count[i - 1] + count[i - 2]
            else:
                # there's only one interpetation (i.e. 57)
                count[i] = count[i - 1]

    print(count)
    return count[n - 1]

# test
print(count_dec("1234"))
