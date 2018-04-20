# Input: abcabca
# Output: 5
# a, ab, abc, abcabc, abcabca

def minimalSteps(s, n):
    dp = [float('inf')] * n

    s1 = ""
    s2 = ""

    dp[0] = 1

    s1 += s[0];

    for i in range(1, n):
        s1 += s[i]
        s2 = s[i + 1:2*(i + 1)]

        #rint("s1 = ", s1)
        print("s2 = ", s2)

        dp[i] = min(dp[i], dp[i - 1] + 1)
        if s1 == s2:
            dp[i * 2 + 1] = min(dp[i] + 1, dp[i * 2 + 1])

    return dp[n - 1];

s = "abcabca"
print(minimalSteps(s, len(s)))
