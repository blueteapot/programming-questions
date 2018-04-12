def three_arrays_intersection(a1, a2, a3):
    x = 0
    y = 0
    z = 0
    res = []

    while x < len(a1) and y < len(a2) and z < len(a3):
        print(a1[x], a2[y], a3[z])

        if a1[x] == a2[y] == a3[z]:
            res.append(a1[x])
            x+=1
            y+=1
            z+=1
        elif a1[x] < a2[y]:
            x +=1
        elif a2[y] < a3[z]:
            y +=1
        else:
            z +=1

    return res

# test
a = [1, 2, 3, 5, 8]
b = [3, 5, 6, 8, 12]
c = [1, 2, 5, 6, 8]

assert(three_arrays_intersection(a,b, c) == [5,8])
print("passed")
