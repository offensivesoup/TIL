import sys
sys.stdin = open('input.txt')


def search(i, j):

    # visited = [[0] * 100] * 100 # 복사된다
    visited = [[0] * 100 for _ in range(100)] # 방문표시용 0으로 채워진 2차원 리스트
    original_j = j # 출발 시점의 j 좌표 기록
    while i != 0: # 탐색 시작 -> x가 99가 될 때 까지
        for dir in [(-1,0),(0,-1),(0,1)]:# 3방향 탐색 아래 왼쪽 오른쪽
            # 현재위치 i, j 를 기준으로 dir[0], dir[1]
            ni = i + dir[0] # 다음 탐색 대상 i좌표값
            nj = j + dir[1] # 다음 탐색 대상 j좌표값
            if 0 <= ni < 100 and 0 <= nj < 100 and arr[ni][nj] == 1 and not visited[ni][nj] == 1: # 세 좌표값이 범위를 벗어나지 않고
                i, j = ni, nj  # 이동
                visited[i][j] = 1  # 내 지금 방문 위치 표시
    return j

for _ in range(10):
    tc = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    # 최종 결과값
    result = 0
    for j in range(100):
        if arr[99][j] == 2:
            result = search(99,j)
    print(result)