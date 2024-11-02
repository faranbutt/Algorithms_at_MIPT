from time import time
L = int(input())
U = int(input())

counter = 0
start = time()
for i in range(U,L,-1):   # Too solwer goes through every number and checks
    counter += 1
    if i % 5 == 0:
        # print(i)
        pass
end = time()
print(f'First loop did {counter} iterations and took {end - start} sec')
print('*****************************************')

counter = 0
start = time()
for i in range(U // 5 * 5,L-1,-5):  # Faster it skips most of the iteration because of -5
    counter +=1                    # Also 12 - 2 = 10
                                 # Also 12 - 7 = 5
end = time()
print(f'Second loop did {counter} iterations and took {end - start} sec')
