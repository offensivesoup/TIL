import sys
sys.stdin = open('input.txt')
from collections import deque
from itertools import combinations

def bfs(que):
    global mini
    while que:
        now = que.popleft()
        d_row = [-1,1,0,0]
        d_col = [0,0,-1,1]
        for i in range(4):
            row = now[0] + d_row[i]
            col = now[1] + d_col[i]
            if 0 <= row < N and 0 <= col < N:
                if area[row][col] != 1 and not visited[row][col]:
                    visited[row][col] = visited[now[0]][now[1]] + 1
                    que.append(((row,col)))
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and area[i][j] != 1:
                return -1
    a = 0
    for visit in visited:
        if max(visit) > a:
            a = max(visit)
    return a


N, M = map(int,input().split())
area = [list(map(int,input().split())) for _ in range(N)]
two_lst = []
for i in range(N):
    for j in range(N):
        if area[i][j] == 2:  # 만약 거기가 2라면
            two_lst.append((i,j,0))
can_virus = list(combinations(two_lst, M))
que = deque([])
mini = 1e9
maxi = []
for virus in can_virus:
    visited = [[0] * N for _ in range(N)]
    for vi in virus:
        visited[vi[0]][vi[1]] = -1
        que.append(vi)
    maxi.append(bfs(que))

if maxi.count(-1) == len(can_virus):
    print(-1)
else:
    for ma in maxi:
        if ma == -1:
            pass
        else:
            if mini > ma:
                mini = ma
    print(mini)

