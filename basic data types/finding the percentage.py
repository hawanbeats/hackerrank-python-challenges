N = int(input())
STUDENT_MARKS = {}

for line in range(N):
    info = input().split(" ")
    grades = list(map(float, info[1:]))
    STUDENT_MARKS[info[0]] = sum(grades) / float(len(grades))

print("%.2f" % round(STUDENT_MARKS[input()], 2))
