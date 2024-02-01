import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int,input().split())
    ballons = [list(map(int,input().split())) for _ in range(N)]
    delta_row = [-1,1,0,0,0]
    delta_col = [0,0,-1,1,0]
    flowerLst = []
    for i in range(1,N-1):
        for j in range(1,M-1):
            total = 0
            for k in range(5):
                row = delta_row[k]
                col = delta_col[k]
                total += ballons[i+row][j+col]               
            flowerLst.append(total)
    print(f'#{test_case} {max(flowerLst)}')