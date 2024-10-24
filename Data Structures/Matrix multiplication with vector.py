def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
    m = len(a)
    if len(a[0]) != len(b):
        return 1
    else:
        dummy = [0] * m
        l = len(dummy)
        for i,j in enumerate(a):
            dummy[i] = sum(j[0]*j[1] for j in  zip(j,b))

    return dummy




a = [[1,2],[2,4]]
b = [1,2]
print(matrix_dot_vector(a,b))