import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1,T+1):
    N, M = map(int,input().split())
    aj = list(map(int,input().split()))
    bj = list(map(int,input().split()))
    maxi = 0
    if M > N:
        for i in range(M-N+1):
            sumi = 0
            for j in range(N):
                sumi += aj[j] * bj[i+j]
            if sumi > maxi:
                maxi = sumi
    elif N > M:
        for i in range(N-M+1):
            sumi = 0
            for j in range(M):
                sumi += bj[j] * aj[i+j]
            if sumi > maxi:
                maxi = sumi
    else:
        for i in range(M):
            maxi += aj[i] * bj[i]
    print(f"#{test_case} {maxi}")
