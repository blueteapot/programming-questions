def all_anagrams(s):
    n = len(s)
    if n == 1:
        return [s]

    permutations = []
    for i in range(n - 1):
        s_i = s[:i] + s[i+1:]
        ch_i = s[i]

        s_i_anagrams = all_anagrams(s_i)
        for j in range(len(s_i_anagrams)):
            permutations += [ch_i + s_i_anagrams[j], s_i_anagrams[j] + ch_i]

    return permutations




# test
print(all_anagrams("ABC"))
