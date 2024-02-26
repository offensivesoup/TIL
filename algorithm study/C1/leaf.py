## 행렬덧셈 2738
# import sys

# N, M = map(int,sys.stdin.readline().split())
# resultA = []
# resultB = []
# for i in range(N):
#     resultA.append(list(map(int,sys.stdin.readline().split())))

# for i in range(N):
#     resultB.append(list(map(int,sys.stdin.readline().split())))    

# for m in range(N):
#     if m > 0:
#         print()
#     for j in range(M):
#         print(resultA[m][j] + resultB[m][j], end = ' ')


## 아스키 코드 11654.
# 아스키를 문자로 바꾸려면 chr
# print(ord(str(input())))

## 단어 길이 재기 2734번
# print(len(str(input())))

## 대소문자 바꾸기 2744

# N = str(input())
# result = ''
# for i in N:
#     if i.isupper():
#         result += i.lower()
#     else:
#         result += i.upper()

# print(result)

## 학점계산 2754

# N = str(input())
# strLst = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D+', 'D0', 'D-', 'F']
# scrLst = [4.3 , 4.0 , 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0]

# for x in range(len(strLst)):
#     if N == strLst[x]:
#         print(scrLst[x])

# ## 문자와 문자열 27866
# while True:
#     try:
#         print(input())
#     except Exception:
#         break

## 문자열 9086번

T = int(input())

for _ in range(T):
    N = str(input())
    print(N[0],N[-1],sep='')

