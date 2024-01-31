# bit = [0,0,0,0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             for l in range(2):
#                 bit[3] = l
#                 print(bit)

## 비트 연산자

# def f(arr, N):
#     for i in range(1, 1 << N):
#         s = 0
#         for j in range(N):
#             if i & (1 << j):
#                 s += arr[j]
#                 # print(arr[j], end=' ')
#         #print(s)
#         if s == 0:
#             return True
#     return False
#
# N = int(input())
# arr = list(map(int, input().split()))
#
# print(f(arr, N))

## 부분집합의 합

'''
10
-7 -5 2 3 8 -2 4 6 0
'''
N = 100
# arr = [-7, -5, 2, 3, 8, -2, 4, 6, 9, 0]
arr = list(range(1,101))
# 부분집합의 합이 55 미만인 경우만 모은 리스트
print(arr)
print(2**10) # 모든 부분집합의 개수
print(2 ** N)
print(1 << N)
print(bin(1024))

for i in range(1, 1 << N):
    lst = []
    print(i, '번째 경우의 수')
    for j in range(N-1, -1, -1):
        # print(1 << j) # 비트가 각각의 고유 번호가 된다.
        # i번째 경우의 수에, j번째 요소가 포함 되어있는 부분 집합인지 확인하는 코드
        # i번째가 3번째라면 -> 0b 0011
        # j번째 요소 (0번째, 1번째, 2번째...) -> 0b 0001, 0010, 0011, ...
        if i & (1 << j):
            lst.append(arr[j])
            if sum(lst) >= 55:
                break
    if sum(lst) < 55:
        print(lst)