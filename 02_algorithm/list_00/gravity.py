'''
입력값
9
7 4 2 0 0 6 0 7 0
7 8 2 0 0 6 0 7 0
'''

## 내코드

N   = int(input()) # 상자가 쌓여있는 가로 길이
arr = list(map(int, input().split()))
maxi = arr.index(max(arr))

result = 0
for idx, value in enumerate(arr):
    if idx > maxi and arr[maxi] > value:
        result += 1
print(result)

## 수업 코드

# N = int(input())
# arr = list(map(int, input().split()))
# max_v = 0
# for i in range(N-1):
#     cnt = 0 # 오른쪽에 있는 더 낮은 높이의 개수
#     for j in range(i+1, N):
#         if arr[i] > arr[j]:
#             cnt += 1
#     if max_v < cnt:
#         max_v = cnt
# print(max_v)
