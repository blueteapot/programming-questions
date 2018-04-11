def lps(s):
    print(s)
    n = len(s)
    if n <= 1:
        return n

    if s[0] == s[n-1]:
        return 2 + lps(s[1:-1])
    return max(lps(s[:-1]), lps(s[1:]))

print(lps("AABDAA"))
