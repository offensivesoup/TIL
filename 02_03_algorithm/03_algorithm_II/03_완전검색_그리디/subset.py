# 0b110이 주어지면
# 1비트가 1인지 확인하는 것

# arr = ['A','B','C','D','E']
# n = len(arr)
#
# # 친구가 2명 들어온다면
# def get_count(tar):
#     cnt = 0
#     for i in range(n):
#         if tar & 0x1: # 1비트가 1인지 확인하는 코드
#             cnt += 1
#         tar >>= 1 # right shift 비트 연산자 -> 오른쪽 끝 비트를 하나씩 제거
#     return cnt
# result = 0
# for tar in range(1 << n):
#     if get_count(tar) >= 2: # bit 가 2개 이상인게 1이라면,
#         result +=1
# print(result)

# 조합 코드

# arr = ['A','B','C','D','E']
# path = []
# n = 3
# def run(lev,start):
#     if lev == n:
#          print(path)
#          return
#
#     for i in range(start, 5):
#         path.append(arr[i])
#         run(lev + 1, i + 1)
#         path.pop()
#
# run(0, 0)


# N = 3
# path = []
#
# def func(lev, start):
#     if lev == N:
#         print(path)
#         return
#
#     for i in range(start,7):
#         path.append(i)
#         func(lev + 1, i)
#         path.pop()
# func(0, 1)

# toilet = [15,30,50,10]
# toilet.sort()
# sumi = 0
# while toilet:
#     a = toilet.pop(0)
#     sumi += (a*len(toilet))
# print(sumi)

# fractional Knapsack 문제

# n = 3
# target = 30
# things = [(5, 50), (10, 60), (20, 140)] # (kg, price)
# things.sort(key = lambda x : (x[1] / x[0]), reverse = True) # kg당 price로 내림차순 정렬
#
# sumi = 0
#
# for kg, price in things:
#     per_price = price / kg
#     # 만약 가방에 남은 용량이 얼마 되지 않는다면, 물건을 잘라 가방에 넣고 끝낸다
#     if target < kg:
#         sumi += target * per_price
#         break
#     sumi += price
#     target -= kg
# print(int(sumi))

## 회의실 선택문제

from collections import deque
#
# time = [(1,4), (3,5), (1,6), (5,7), (3,8), (5,9), (6,10), (8,11), (2,13), (12,14)]
# time.sort(key = lambda x : x[1])
# cnt = 0
# while time:
#     for t in time:
#






