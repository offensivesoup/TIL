import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs(que):
    while que:
        now = que.popleft()
        x = now[0]
        y = now[1]
        delta_row = [-1,1,0,0]
        delta_col = [0,0,-1,1]
        for i in range(4):
            row = x + delta_row[i]
            col = y + delta_col[i]
            if 0 <= row < N and 0 <= col < N:
                if not visited[row][col]:
                    visited[row][col] = 1
                    que.append((row,col))

N = int(input())
area = []
maxi = 0
for i in range(N):
    line = list(map(int,input().split()))
    maxi = max(max(line), maxi)

    area.append(line)

result = 0
for rain in range(0, maxi):
    high = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if area[i][j] <= rain:
                visited[i][j] = rain
    for m in range(N):
        for n in range(N):
            if not visited[m][n]:
                start = deque([(m,n)])
                bfs(start)
                high += 1
    if high > result:
        result = high

print(result)