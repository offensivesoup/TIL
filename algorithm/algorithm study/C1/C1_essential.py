## 최대값 출력

# arr = [int(input()) for _ in range(9)]
# print(max(arr))
# print(arr.index(max(arr))+1)

## 문자열 반복

# T = int(input())

# for test_case in range(T):
#     R, S = input().split()
#     for char in S:
#         print(char*int(R),end = '')
#     print()

## 최소,최대

# N = int(input())
# arr = list(map(int,input().split()))
# print(f'{min(arr)} {max(arr)}')

## 숫자의 합

# N = int(input())
# num = input()
# result = 0
# for i in range(N):
#     result += int(num[i])
# print(result)

## 문자열 세기

# char = input().split()
# print(len(char))

## 단어공부

# word = input().upper()
# wordLst = []
# wordDict = {}
# maxLst = []
# for i in range(len(word)):
#     wordLst.append(word[i])
# for char in set(wordLst):
#     wordDict[char] = wordLst.count(char)
# for var in wordDict:
#     if wordDict[var] == max(wordDict.values()):
#         maxLst.append(var)
# if len(maxLst) >= 2:
#     print('?')
# else:
#     print(*maxLst)