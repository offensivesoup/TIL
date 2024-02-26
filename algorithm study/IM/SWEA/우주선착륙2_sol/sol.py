import sys
sys.stdin = open('input.txt')

T = int(input())

d_row = [-1,1,0,0,-1,-1,1,1]
d_col = [0,0,-1,1,-1,1,-1,1]

def search(x,y, Lst):
    cnt = 0
    for m in range(8):
        row = x + d_row[m]
        col = y + d_col[m]
        if 0 <= row < N and 0 <= col < M:
            if moon[row][col] < moon[x][y]:
                cnt += 1
    Lst.append(cnt)

for test_case in range(1,T+1):
    tmpLst = []
    N, M = map(int,input().split())
    moon = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            search(i,j,tmpLst)
    candidate = 0
    for t in tmpLst:
        if t >= 4:
            candidate += 1
    print(f"#{test_case} {candidate}")
    
            
        