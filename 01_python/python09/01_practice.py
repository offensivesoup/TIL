import sys

# 파이썬에서 데이터를 입력받는 함수
# num1 = int(input()) # 입력받은 값을 문자열로 반환
# num2 = int(input())
# result = num1 + num2
# print(result)


# 2번 입력 받는다 -> for 사용해서 2번 똑같은코드
# 근데 2번 입력 받은 값을.. 더해서 출력해야하는데 ...

# result = 0
# for i in range(2):
#     num = int(input())
#     result += num
# print(result)

# txt 파일의 각 줄의 내용을
# input 함수가 실행될때마다 넣어준다.

# sys.stdin = open('input.txt') # stdin에 담긴다.

# N = int(input())
# N번 만큼 입력이 주어진다 했으니, N번만큼 반복해서 input
# result = []
# for i in range(N):
#     # str.splie() => 공백을 기준으로 쪼개서 리스트에 담음
#     arr = input().split()
#     # 모든 요소 순회해서 정수로 바꿔서 다시 리스트 만들기
#     digit_list = []
#     for num in arr:
#         digit_list.append(int(num))
#     result.append(digit_list)
# print(result)
# num = 0
# for i in result:
#     for j in i:
#         num += j
# print(num)

# result = []
# for i in range(N):
#     arr = list(map(int, input().split()))
#     result.append(arr)

# result = [list(map(int, input().split())) for _ in range(N)]
# print(result)




# arr1 = input()
# arr2 = input()
# arr3 = input()

# print(N)
# print(arr1)
# print(arr2)
# print(arr3)

# 거꾸로 출력

# sys.stdin = open('input.txt')

# N = int(input())

# for i in range(N,-1,-1):
#     print(i)

# n줄 덧셈
    
# sys.stdin = open('input.txt')
# N = int(input())

# ## 입력으로 자연수 number가 주어질 때, 1부터 주어진 자연수 number까지를 모두 더한 값을 출력하시오.

# result = 0
# for i in range(1,N+1):
#     result += i
# print(result)

## solution.py

# sys.stdin = open('input.txt')
# N = int(input())

# for i in range(1,N+1):
#     print(' '*(N-i),'*'*i,sep = '')

## 2차원 리스트 전체합 구하기

sys.stdin = open('input.txt')
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0
for Lst in arr:
    for j in Lst:
        result += j
print(result)

