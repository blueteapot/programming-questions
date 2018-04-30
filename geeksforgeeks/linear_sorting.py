# assumption, values are between 0-9
def counting_sort(A):
    n = len(A)
    B = [0] * n
    C = [0] * 10

    for i in range(n):
        C[A[i]] += 1

    print(C)

    for i in range(1, len(C)):
        C[i] += C[i - 1]

    print(C)

    for i in range(n - 1, -1, -1):
        val = A[i]
        B[C[val] - 1] = val
        C[val] -= 1

    return B
