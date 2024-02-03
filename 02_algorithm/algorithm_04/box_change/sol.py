import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, Q = map(int,input().split())
    zeroLst = [0] * N
    boxLst = [list(map(int,input().split())) for _ in range(Q)]
    for i in range(Q):
        for j in range(N):
            if boxLst[i][0]-1 <= j <= boxLst[i][1]-1:
                zeroLst[j] = i+1
    print(f'#{test_case}', end = ' ')
    for zero in zeroLst:
        print(zero, end = ' ')
    print()
