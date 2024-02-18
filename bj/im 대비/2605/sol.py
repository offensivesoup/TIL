'''
한 줄로 줄을 서고, 첫째부터 차례로 번호 뽑음
첫째는 무조건 0번 뽑음(고정)
둘째는 (0,1) , 셋째는 (0,1,2) ~
'''

from collections import deque
# N = int(input()) # 학생수
# number = list(map(int,input().split())) # 뽑는 번호표
# result = []
# for i in range(N):
#     result.insert(number[i],i+1)
# result.reverse()
# print(*result)

# N = int(input()) # 학생수
# number = list(map(int,input().split())) # 뽑는 번호표
# result = deque([1])

# for i in range(1,N+1):
#     if i < N:
#         cnt = 1
#         if number[i-cnt] == number[i]:
#             result.insert(number[i],i)
#         else:
#             while True:
#                 cnt += 1
#                 if number[i-cnt] <= number[i]:
#                     result.insert(number[i-cnt-1],i)
#                     break            
# print(result)
