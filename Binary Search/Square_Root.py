def square_root(x):
    L = 0
    R = x
    while L <= R:
        M = (L+R) // 2
        M_2 = M * M
        if M_2 == x:
            return M
        elif M_2 > x:
            R = M - 1
        else:
            L = M + 1
    return R


print(square_root(16))