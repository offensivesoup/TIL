from collections import deque
import sys
sys.stdin = open('input.txt')

## 다 녹이고, 빙산의 개수를 세어보는 함수
def bfs(que):
    while que:
        now = que.popleft()
        delta_row = [-1,1,0,0]
        delta_col = [0,0,-1,1]
        for j in range(4):
            row = now[0] + delta_row[j]
            col = now[1] + delta_col[j]
            if 0 <= row < N and 0 <= col < M:
                if ice_mountain[row][col] and melting[row][col] != 'melt' and not visited[row][col]: # 안녹았음
                    visited[row][col] = 1
                    que.append((row, col)) # 그럼 넣어줄꺼야
    return 1

# 빙하를 녹여보는 함수
def one_year(point):
    x = point[0]
    y = point[1]
    delta_row = [-1,1,0,0]
    delta_col = [0,0,-1,1]
    for i in range(4):
        row = x + delta_row[i]
        col = y + delta_col[i]
        if 0 <= row < N and 0 <= col < M and (ice_mountain[row][col] == 0 or melting[row][col] =='melt'):
            melting[x][y] += 1 # 이만큼 녹여버릴거야

N, M = map(int,sys.stdin.readline().split())
ice_mountain = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
melting = [[0] * M for _ in range(N)]
result = 0
cnt = 0
while True:
    check = 0
    visited = [[0] * M for _ in range(N)]
    for n in range(N):  
        for m in range(M):
            if (ice_mountain[n][m] and melting[n][m] != 'melt' and not visited[n][m]):
                visited[n][m] = 1
                cnt += bfs(deque([(n,m)]))
    if cnt >= 2:
        break
    cnt = 0
    result += 1
    for i in range(N):
        for j in range(M):
            if (ice_mountain[i][j] and melting[i][j] != 'melt'): # 다 안녹았음
                one_year((i,j)) # 녹여볼거야
    for k in range(N):
        for l in range(M):
            if melting[k][l] != 'melt':
                if ice_mountain[k][l] - melting[k][l] <= 0:
                    melting[k][l] = 'melt'
            else:
                check += 1
    if check == N*M:
        result = 0
        break
print(result)