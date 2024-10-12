import sys
sys.stdin = open('input.txt', 'r')
lines = sys.stdin.readlines()
N = len(lines) - 1
students = []
for i in range(1, N + 1):
    id, score, nickname = lines[i].split()
    students.append([int(id), int(score), nickname])
for i in range(N):
    for j in range(0, N-i-1):
        if students[j][1] < students[j+1][1]:
            students[j], students[j+1] = students[j+1], students[j]
        elif students[j][1] == students[j+1][1] and students[j][0] > students[j+1][0]:
            students[j], students[j+1] = students[j+1], students[j]
print(students[0][2])
print(students[1][2])
print(students[2][2])
for student in students:
    print(student[0], end=' ')

