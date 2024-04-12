import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs(que):
    while que:
        point = que.popleft()
        x = point[0]
        y = point[1]
        delta_row = [-1,1,0,0]
        delta_col = [0,0,-1,1]
        for i in range(4):
            row = x + delta_row[i]
            col = y + delta_col[i]
            if 0 <= row < N and 0 <= col < M:
                if not visited[row][col] and miro[row][col]:
                    visited[row][col] = visited[x][y] + 1
                    que.append((row,col))
        

N, M = map(int,input().split())
result = 1e9
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
miro = [list(map(int,list(sys.stdin.readline().strip()))) for _ in range(N)]
goal = (N-1, M-1)
que = deque([(0,0)])
bfs(que)
print(visited[N-1][M-1])

# def dfs(point):
#     global result
#     x = point[0]
#     y = point[1]
#     cnt = point[2]
#     if cnt > result:
#         return
#     delta_row = [-1,1,0,0]
#     delta_col = [0,0,-1,1]
#     if x == N - 1 and y == M - 1:
#         if result > cnt:
#             result = cnt
#     for i in range(4):
#         row = x - delta_row[i]
#         col = y - delta_col[i]
#         if 0 <= row < N and 0 <= col < M:
#             if not visited[row][col] and miro[row][col] == 1:
#                 visited[row][col] = 1
#                 dfs((row,col,cnt+1))
#                 visited[row][col] = 0
                
                 
   
