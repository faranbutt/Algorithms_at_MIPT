import random
def partition(x,l,r,pivot):
    il = l
    ir = r
    i = l
    while i < ir:
        if x[i] < pivot:
            x[il],x[i] = x[i],x[il]
            il+=1
            i += 1
        elif x[i] > pivot:
            ir -= 1
            x[i],x[ir] = x[ir],x[i]
        else:
            i+=1
    return il,ir




def qsort(x,l=0,r=None):
    if r is None:
        r = len(x)
    if (r-l) > 1:
        pivot = x[random.randint(l,r-1)]
        il , ir = partition(x,l,r,pivot)
        qsort(x,l,il)
        qsort(x,ir,r)


if __name__=='__main__':
    N = int(input())
    x= list(map(int,input().split()))
    qsort(x)
    print(' '.join(map(str,x)))