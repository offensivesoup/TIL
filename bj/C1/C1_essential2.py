## 별찍기

# N = int(input())
# for i in range(N):
#     print(' '*(N-i-1),'*'*(i+1),sep = '')

## 검증수

# total = 0
# num = map(int,input().split())
# for n in num:
#     total += n**2
# print(total%10)

## 숫자의 개수

# A = int(input())
# B = int(input())
# C = int(input())

# num = A * B * C

# arr = [0] * 10

# for i in str(num):
#     arr[int(i)] += 1
# for result in arr:
#     print(result)

## 알람시계

# hour, minute = map(int,input().split())

# if minute - 45 < 0:
#     if hour == 0:
#         print(23, minute + 15)
#     else:
#         print(hour - 1, minute + 15)
# else:
#     print(hour, minute - 45)

## 음계

# arr = list(map(int,input().split()))
# if arr == [1,2,3,4,5,6,7,8]:
#     print('ascending')
# elif arr == [8,7,6,5,4,3,2,1]:
#     print('descending')
# else:
#     print('mixed')

## 나머지

# arr = [int(input()) for _ in range(10)]
# total = [x % 42 for x in arr]
# result = len(set(total))
# print(result)

## OX 점수

# T = int(input())
# for test_case in range(1,T+1):
#     ox = input()
#     idx = 0
#     plus = 1
#     sumi = 0
#     total = 0
#     while idx < len(ox):
#         if ox[idx] == 'O':
#             sumi += plus
#             plus += 1
#         elif ox[idx] == 'X':
#             total += sumi
#             sumi = 0
#             plus = 1
#         if idx == len(ox) -1:
#             total += sumi
#         idx += 1
#     print(total)

## ACM 호텔

# T = int(input())
# for test_case in range(T):
#     H, W, N = map(int,input().split())
#     son = 0
#     for w in range(1,W+1):
#         for h in range(1,H+1):
#             son += 1
#             if son == N:
#                 if w < 10:
#                     print(h,0,w,sep='')
#                 else:
#                     print(h,w,sep='')
        

## 알파벳 찾기
N = input()
word = [x for x in N]
arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
arr2 = [-1] * len(arr)
for i in range(len(arr)):
    for w in range(len(word)):
        if word[w] == arr[i]:
            arr2[i] = w
print(*arr2)