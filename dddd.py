import sys
N, M = map(int,sys.stdin.readline().split())
resultA = []
resultB = []
for i in range(N):
    resultA.append(list(map(int,sys.stdin.readline().split())))

for n in range(M):
    resultB.append(list(map(int,sys.stdin.readline().split())))

for m in range(N):
    for j in range(M):
        print(resultA[m][j] + resultB[m][j], end = ' ')
    print()