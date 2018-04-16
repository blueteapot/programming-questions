def replaceall0with5(num):
    res = 0
    i = 0

    if num == 0:
        return 5

    while num > 0:
        digit = num % 10
        num = int(num / 10)

        if digit == 0:
            digit = 5

        res += digit * 10**i
        i+=1

    return res

# test
assert(replaceall0with5(0) == 5)
assert(replaceall0with5(5) == 5)
assert(replaceall0with5(105) == 155)
assert(replaceall0with5(123456) == 123456)
assert(replaceall0with5(1010) == 1515)

print("passed")
