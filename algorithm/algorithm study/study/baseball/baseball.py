import sys
from itertools import permutations
from copy import deepcopy
sys.stdin = open('input.txt')

N = int(input())
baseball = list(permutations([1,2,3,4,5,6,7,8,9],3))
result   = deepcopy(baseball)
for _ in range(N):
    num, strike, ball = map(int,input().split())
    number = tuple(map(int,str(num)))
    for b in range(len(baseball)):
        s_cnt = 0  # 스트라이크 세볼거임
        b_cnt = 0  # 볼 세볼거임
        for i in range(3):
            if baseball[b][i] == number[i]:
                s_cnt += 1
            elif baseball[b][i] in number:
                b_cnt += 1
        if s_cnt != strike or b_cnt != ball:
            if baseball[b] in result:
                result.remove(baseball[b])
print(len(result))