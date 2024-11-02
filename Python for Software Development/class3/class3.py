from collections import Counter


l  = [12,5,1,5,2,3,5,1,23,12,1,1,1,2,2,4,5]
a = Counter(l)
print(a)


d1= {
    1:2,
    2:3,
    4:4,
}

d2 = {
    1:2,
    2:4,
    3:8,
}

print(d1 | d2) #union
print(d1.keys() & d2.keys()) #intersection

li = [1,2,2,3,4,1,5,2,3,4,5,6]
dummy = {}
for i in li:
    if i not in dummy:
        dummy[i] = 1
    else:
        dummy[i] += 1
print("COUNTER",dummy)