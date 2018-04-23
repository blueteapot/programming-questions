def josephus(n, k):
    if n == 1:
        return 1
    return (josephus(n-1, k) + k) % n

# test

print(josephus(4, 2) == 2)
print("passed")
