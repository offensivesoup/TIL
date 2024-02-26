import sys
sys.stdin = open('input.txt')

T = int(input())
money = [50000,10000,5000,1000,500,100,50,10]

for test_case in range(1,T+1):
    N = int(input()) # 돈
    cnt   = [0] * 8
    for i in range(len(money)):
        c = 0
        if money[i] <= N:
            c = N // money[i]
            N -= money[i] * c
        cnt[i] = c
    print(f'#{test_case}')
    print(*cnt)