import sys
sys.stdin = open('input.txt')

from collections import deque

## 풍선 추가로 터질 때 로직

# def pang():
#     result = []
#     for i in range(N):
#         for j in range(M):
#             result.append(add_ballons((i,j)))
#     print(result)
#     return max(result)


# def add_ballons(point):
#     adding = ballons[point[0]][point[1]]
#     pangcnt = adding
#     row = point[0]
#     col = point[1]
#     for add in range(1,adding+1):
#         if row + add < N:
#             pangcnt += ballons[row+add][col]
#         if 0 <= row - add:
#             pangcnt += ballons[row-add][col]
#         if col + add < M:
#             pangcnt += ballons[row][col+add]
#         if 0 <= col - add:
#             pangcnt += ballons[row][col-add]
#     return pangcnt 

# T = int(input())

# for test_case in range(1,T+1): # 테스트 케이스
#     N, M = map(int,input().split()) # N 은 행 개수, M은 열 개수
#     ballons = [list(map(int,input().split())) for _ in range(N)] # 풍선 입력
#     print(pang())

## 그냥 풍선 터트리기 로직

def pang():
    result = []
    for i in range(N):
        for j in range(M):
            result.append(delta_ballons((i,j)))
    return max(result)


def delta_ballons(point):
    adding = ballons[point[0]][point[1]]
    pangcnt = adding
    for m in range(4):
        row = point[0] + d_row[m]
        col = point[1] + d_col[m]
        if 0 <= row < N and 0 <= col < M:
            pangcnt += ballons[row][col]
    return pangcnt 


T = int(input())

d_row = [-1,1,0,0]
d_col = [0,0,-1,1]

for test_case in range(1,T+1): # 테스트 케이스
    N, M = map(int,input().split()) # N 은 행 개수, M은 열 개수
    ballons = [list(map(int,input().split())) for _ in range(N)] # 풍선 입력
    print(f'#{test_case} {pang()}')
