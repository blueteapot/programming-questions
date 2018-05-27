## https://www.geeksforgeeks.org/longest-common-substring/
##
##
def LCS(s1, s2):
    n1 = len(s1)
    n2 = len(s2)

    # dp[x][y] is the LCS for s1[0:x] and s2[0:y]
    dp = [[-1] * n2 for i in range(n1)]

    for i in range(n1):
        dp[i][0] = 1 if s1[i] == s2[0] else 0

    for i in range(n2):
        dp[0][i] = 1 if s2[i] == s1[0] else 0


    for i in range(1, n1):
        for j in range(1, n2):
            if s1[i] != s2[j]:
                dp[i][j] = max(max(dp[i-1][j], dp[i-1][j-1]), dp[i][j-1])
            else:
                dp[i][j] = max(max(dp[i - 1][j - 1] + 1, dp[i - 1][j]), dp[i][j - 1])

    # print dp mat
    # for i in range(n1):
    #     line = ""
    #     for j in range(n2):
    #         line += str(dp[i][j]) + "\t"
    #     print(line)

    return dp[n1 - 1][n2 - 1]

def longest_palindrom(s1):
    s1_reversed = ''.join(reversed(s1))
    return LCS(s1, s1_reversed)

# test
print(LCS("abcdxyz", "xyzabcd"))
print(longest_palindrom("abaacaaba"))
