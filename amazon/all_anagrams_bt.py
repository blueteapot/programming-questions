# https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
# Time Complexity: O(n*n!) Note that there are n! permutations
# and it requires O(n) time to print a a permutation.

def all_anagrams_bt_helper(s, low, high):
    if low == high:
        print(s)
    else:
        for i in range(low, high):
            s[low], s[i] = s[i], s[low]
            all_anagrams_bt_helper(s, low + 1, high)
            s[low], s[i] = s[i], s[low] # backtrack

def all_anagrams_bt(s):
    all_anagrams_bt_helper(s, 0, len(s))

# test
all_anagrams_bt(['A', 'B', 'C'])
