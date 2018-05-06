def encrypt(s, key):
    idx = 0
    enc = ""
    n = len(s)
    for i in range(n):
        enc += s[idx]
        idx += key + 1
        idx = idx % n

    return enc




print(encrypt("defend the east wall", key = 3))
