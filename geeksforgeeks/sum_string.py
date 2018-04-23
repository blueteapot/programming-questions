# https://www.geeksforgeeks.org/check-given-string-sum-string/


# TODO: incorrect!

def is_sum_string(s):

    n = len(s)

    if n < 3:
        return True

    for i in range(1, n):
        for j in range(i + 1, n):
            print("s1 = ", s[i:j], " s2 = ", s[j:j], " s3 = ", s[j:n], ", s4 = ", s[i:n])
            n1 = int(s[0:i])
            n2 = int(s[i:j])
            n3 = int(s[j:n])

            #print(n1, n2, n3)

            if n1 + n2 == n3:
                print("Hoooray!", s[0:j])
                b = is_sum_string(s[0:j])
                if b == True:
                    return b

    return False


# test
print(is_sum_string("12243660"))
