import sys
sys.stdin = open('input.txt')
from itertools import combinations
'''
1 2로 10을 만들려면
어차피 2를 1 2개로 만들 수 있다는 경우를 가정
dp = [0,0,0,0,0,0,0,0,0,0,0]
개수로 따졌을때
1.
1 2로 1000을 만드는 것은
1로 1000을 만드는 것 하나와
나머지 천개짜리 1을
2개씩 2로 바꾸어주는 것 500개 해서
501개 이다.
'''
T = int(input())
for test_case in range(T):
    N = int(input())
    coins = list(map(int,input().split())) # 각 동전이 주어진다.
    goal  = int(input()) # 해당 금액을 만들면된다.
    dp = [0] * (goal+1)
    for c in coins:
        dp[c] = 1   # 얘넨 이미 가지고 있는 동전
    for i in range(min(coins)+1,goal+1): # 최소값에서 돌려서
        for coin in coins: # 코인들을 돌림
            if dp[i-coin]:
                dp[i] = max(dp[i], dp[i-coin] + 1)


    print(dp)