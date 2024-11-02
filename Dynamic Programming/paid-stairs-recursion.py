def stairs_rec(n):
    if len(n)<=2:
        return n[-1]
    d1 = n[0] + stairs_rec(n[1:])
    d2 = n[1] + stairs_rec(n[2:])
    return min(d1,d2)


n = [0,1,2,15,2,30,3]
print(stairs_rec(n))