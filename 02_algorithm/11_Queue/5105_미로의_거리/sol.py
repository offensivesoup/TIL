import sys
sys.stdin = open('input.txt')
#
from collections import deque

def delta_move(point, area, visited):
    delta_lst = [] # 너비탐색 리스트
    delta_row = [-1,1,0,0]
    delta_col = [0,0,-1,1]
    for i in range(4): # 델타 탐색
        row = point[0] + delta_row[i]
        col = point[1] + delta_col[i]
        if 0 <= row < N and 0 <= col < N:
            if area[row][col] == 0 and visited[row][col] == 0:
                delta_lst.append((row, col)) # 리스트에 다 추가
            elif area[row][col] == 3:
                delta_lst.append((row, col))
    if delta_lst: # 갈 수 있는 지점이 있으면
        return delta_lst # 리스트 반환

def bfs(S, G, area, N):
    q = deque()
    q.append(S)
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[S[0]][S[1]] = 1 # 시작지점 방문표시
    while q:
        p, p2 = q.popleft() # 큐 하나 빼보고
        moving = delta_move((p,p2), area, visited) # 델타 이동시킴
        if moving: # 돌아온게 있으면
            for l in moving: # 그거 하나씩 빼봄
                if l == G: # 만약 골인지점 갔으면
                    return visited[p][p2] - 1 # 해당 지점의 방문값 반환
                else:
                    visited[l[0]][l[1]] = visited[p][p2] + 1 # 거기에 방문 표시
                    q.append(l) # 큐에 갔던 곳 넣음
        else: # 온게 없으면
            continue # 다시 빼러 가봄
    return 0 # 다 통과햇는데 결승점 못가면 0

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    start = 0
    goal  = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = (i,j)
            elif arr[i][j] == 3:
                goal  = (i,j)
    print(f'#{test_case} {bfs(start, goal, arr, N)}')