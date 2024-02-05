## 2차원 배열의 선언

# N = int(input())
# arr = [list(map(int,input().split())) for _ in range(N)]
# arr2 = [[0] * N for _ in range(N)]
# arr3 = [[0]*N]*N
# print(arr3)
# arr3[0][0] = 1
# print(arr3)

## 순회하는 법

## 행 우선 순회
#
# for i in range(n):
#     for j in range(m):
#         f(array[i][j])

## 열 우선 순회

# for j in range(m):
#     for i in range(n):
#         f(array[i][j])

## 지그재그 순회

# for i in range(n):
#     for j in range(m):
#         f(array[i][j + (m-1-2*j) * (i%2)])

# # 델타를 이용한 2차 배열 탐색
#
# N  = 5
# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# arr = [[0] * N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         for k in range(4):
#             ni = i + di[k]
#             nj = j + dj[k]
#             if 0 <= ni < N and 0 <= nj < N:
#                 print(arr[ni][nj], end = ' ')
#         print()
#
# i  = 3
# j  = 4
#
#
# for k in range(4):
#     ni = i + di[k]
#     nj = j + dj[k]
#     print(ni, nj)
#
# #한 좌표에서 4방향의 인접 배열 요소를 탐색하게 된다.
#
# N  = 5
# arr = [[0] * N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
#             ni, nj = i +di, j + dj
#             if 0 <= ni < N and 0 <= nj < N:
#                 print(arr[ni][nj])

## 전치행렬
# arr = [[1,2,3],[4,5,6],[7,8,9]]
# for i in range(3):
#     for j in range(3):
#         if i < j: # if 문이 없다면 2번 바꿔서 전치행렬이 가능하지 않는다.
#             arr[i][j], arr[j][i] = arr[j][i], arr[i][j]