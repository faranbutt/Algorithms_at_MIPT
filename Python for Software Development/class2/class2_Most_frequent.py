import sys
sys.stdin = open('../input.txt', 'r')
grades = list(map(int,sys.stdin.readlines()))
N = grades[0]
most_freq_counter = 0
most_freq_grade = None
#
# for i in range(1,N):
#     counter = 0
#     for j in range(1,N):
#         if grades[i] == grades[j]:
#             counter+=1
#     print(f'{grades[i]} -> {counter}')
#     if counter > most_freq_counter:
#         most_freq_counter = counter
#         most_freq_grade = grades[i]
# print(f"Most Freq Greade is {most_freq_grade}")
for i in range(0,N,1):
    number = grades[i]
    counter = grades.count(number)
    print(counter)


l = [1,25,6,12]
s = l[::]
l[0] = 22
print(l)
print(s)