def longest_inc_seq(lst):
    n = len(lst)
    dp = [1] * n

    for i in range(1, n):
        max = 1
        for j in range(i):
            if lst[i] > lst[j]:
                if dp[j] + 1 > max:
                    max = dp[j] + 1

        dp[i] = max

    print(dp)
    print(lst)



longest_inc_seq([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
