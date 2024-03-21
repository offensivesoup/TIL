import sys
sys.stdin = open('input.txt')

from heapq import heappop, heappush

## 4방향 델타탐색
def dijkstra(point, heap):
    d_row = [-1,1,0,0]
    d_col = [0,0,-1,1]
    for i in range(4):
        row = point[0] + d_row[i]
        col = point[1] + d_col[i]
        if 0 <= row < N and 0 <= col < N:
            if dist[row][col] > point[2] + 1 + max(0, area[row][col] - area[point[0]][point[1]]):
                dist[row][col] = point[2] + 1 + max(0, area[row][col] - area[point[0]][point[1]])
                heappush(heap, [row, col, dist[row][col]])

T = int(input())
INF = 1e9
for test_case in range(1, T+1):
    N = int(input()) # 칸수
    area = [list(map(int,input().split())) for _ in range(N)]
    dist = [[INF] * N for _ in range(N)] # 2차원 배열이니까 거리도
    heap = [[0,0,0]] # 젤 시작점은 0,0 에 가중치도 0이다.
    dist[0][0] = 0 # 일단 시작점 표시
    sumi = 0 # 가중치 다 더해줄거야
    while heap: # 일단 힙이면
        s, e, w = heappop(heap) # 최소비용을 꺼내준다.
        if s == N-1 and e == N-1: # 도착점에 도착
            sumi = w # 그때의 가중치 배정
            break

        if w != dist[s][e]: # 이미 나온적이 있다면
            continue
        
        dijkstra((s,e,w), heap)
    
    print(f'#{test_case} {sumi}')
    

