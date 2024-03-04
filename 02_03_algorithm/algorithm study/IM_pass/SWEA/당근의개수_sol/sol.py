import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    C = list(map(int,input().split()))
    cnt = 1
    maxi = 1
    for i in range(1,N):
        if C[i] > C[i-1]:
            cnt += 1
            if maxi < cnt:
                maxi = cnt
        else:
            cnt = 1
    print(f'#{test_case} {maxi}')