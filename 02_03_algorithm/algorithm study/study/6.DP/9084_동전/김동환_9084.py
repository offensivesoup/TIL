import sys
sys.stdin = open('input.txt')
from itertools import combinations
'''
1 2로 10을 만들려면
어차피 2를 1 2개로 만들 수 있다는 경우를 가정
dp = [0,0,0,0,0,0,0,0,0,0,0]

'''
T = int(input())
for test_case in range(T):
    N = int(input())
    coins = list(map(int,input().split())) # 각 동전이 주어진다.
    goal  = int(input()) # 해당 금액을 만들면된다.
    dp = [0] * (goal+1)
    combi = []
    