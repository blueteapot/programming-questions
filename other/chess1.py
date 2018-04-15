# check if queen is threatening king

def q_attack_k(queen_coords, king_coords):
    qx = queen_coords[0]
    qy = queen_coords[1]
    kx = king_coords [0]
    ky = king_coords[1]

    return kx == qx or ky == qy or (abs(kx - qx) == abs(ky - qy))

assert(q_attack_k((1, 1), (2, 2)))
assert(q_attack_k((3, 1), (1, 3)))
assert(q_attack_k((7, 8), (2, 2)) == False)
print("passed")
