import sys
sys.stdin = open('input.txt')
from collections import deque
## 시작점 찾기과 도착점 찾기

def find_start(area):
    for i in range(16):
        for j in range(16):
            if area[i][j] == 2:
                return [i,j]

def find_end(area):
    for i in range(16):
        for j in range(16):
            if area[i][j] == 3:
                return [i,j]

# 움직일 수 있는 지점 찾기

def delta_move(point, area, visited):
    d_row = [-1,1,0,0]
    d_col = [0,0,-1,1]
    for i in range(4):
        row = d_row[i]
        col = d_col[i]
        if area[point[0]+row][point[1]+col] == 0 and visited[point[0]+row][point[1]+col] != 1:
            return [point[0]+row,point[1]+col]
        elif area[point[0]+row][point[1]+col] == 3:
            return [point[0]+row,point[1]+col]
        else:
            continue


## 깊이우선탐색

def bfs(S,G,area):
    stack = [S] # 스택 생성
    visited = [[0 for _ in range(16)] for _ in range(16)] # 방문 표시\
    visited[S[0]][S[1]] = 1
    while stack:
        p = stack[-1] # 처음꺼 빼줄거임
        result = delta_move(p,area,visited)
        if result == G: # 도착했으면
            return 1 # 1반환
        if result:# 주변에 갈 수 있는 통로가 있으면
            stack.append(result) # 그 결과를 큐에 더할게
            visited[result[0]][result[1]] = 1 # 방문표시도 할거야
        else: #못간다면
            stack.pop() # 계속 빼볼거임
    return 0



T = 10
for test_case in range(1,T+1):
    T_num = int(input())
    arr = [list(map(int,input())) for _ in range(16)]
    S = find_start(arr)
    G = find_end(arr)
    result = bfs(S,G,arr)
    print(f'#{test_case} {result}')