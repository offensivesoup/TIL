## bubble_sort

N = int(input())
numLst = [list(map(int,input().split())) for _ in range(N)]

x = 0
y = 1

for i in range(N-1,0,-1):
    for j in range(i):
        if numLst[j][x] > numLst[j+1][x]:
            numLst[j], numLst[j+1] = numLst[j+1], numLst[j]
        elif numLst[j][x] == numLst[j+1][x]:
            if numLst[j][y] > numLst[j+1][y]:
                numLst[j], numLst[j+1] = numLst[j+1], numLst[j]

for number in numLst:
    print(number[0],number[1])