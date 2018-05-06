def is_valid_string(s):
    cnt = 0
    for i in range(len(s)):
        if s[i] == '(':
            cnt += 1
        elif s[i] == ')':
            cnt -= 1

        if cnt < 0:
            return False

    return cnt == 0


print_all_valid(s):
    pass

# test
print_all_valid("(())((")
