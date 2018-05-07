MAX_CHARACTERS = 256

# TODO: code fails - need to count matches instead of just comparing histograms!

def hist_eq(hist_s, hist_t):
    for i in range(MAX_CHARACTERS):
        if hist_t[i] > 0:
            if hist_t[i] != hist_s[i]:
                return False
    return True

def min_angram(s, t):
    n_t = len(t)
    n_s = len(s)

    if t > s:
        return -1

    # start with an initial window
    hist_t = [0] * MAX_CHARACTERS
    hist_s = [0] * MAX_CHARACTERS

    for i in range(n_t):
        hist_t[ord(t[i])] += 1
        hist_s[ord(s[i])] += 1


    start = 0
    end = n_t - 1
    min_len = float('inf')
    min_start = -1
    min_end = -1

    while start < n_s:
        if hist_eq(hist_s, hist_t):
            print("hist_eq")
            if end - start + 1 < min_len:
                min_len = end - start + 1
                min_start = start
                min_end = end
            hist_s[ord(s[start])] -= 1
            start += 1

        elif end < n_s - 1:
            print(s[end])
            end += 1
            hist_s[ord(s[end])] += 1
        else:
            break

    return s[min_start:min_end]


# test
print(min_angram("adobecodebanc", "abc"))
