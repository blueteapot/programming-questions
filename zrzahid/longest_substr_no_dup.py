def longest_substr_no_dup(s):
    n = len(s)
    last = {}
    start = 0
    longest = 0
    for i in range(n):
        #print(start, i, last)
        if s[i] in last:
            if longest < i - start:
                longest = i - start
            start += 1

        last[s[i]] = i

    return longest

# test
assert(longest_substr_no_dup("abcabc") == 3)
assert(longest_substr_no_dup("bbbbbbbbbbbbb") == 1)
assert(longest_substr_no_dup("abcdcdba") == 4)
assert(longest_substr_no_dup("abcxyxabc") == 5)
assert(longest_substr_no_dup("abababababab") == 2)

print("success")
