N=int(input())
students=list()
for i in range(N):
    name = input()
    score = float(input())
    students.append([name,score])
scores=set(students[i][1]for i in range(N))
scores=list(scores)
scores.sort()
students=[x[0] for x in students if x[1]==scores[1]]
students.sort()
for s in students:
    print(s)