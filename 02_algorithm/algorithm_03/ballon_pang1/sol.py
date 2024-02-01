import sys
sys.stdin = open('input.txt')
'''
경우의 수를 나누어 보아야함
각 꼭지점 (더할게 두번임)
각 변의 중간 (더할게 세번임)
중간값들  (더할게 네번임)
'''
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int,input().split())
    ballons = [list(map(int,input().split())) for _ in range(N)]
    delta_row = [-1,1,0,0,0]
    delta_col = [0,0,-1,1,0]
    flowerLst = []
    for i in range(N):
        for j in range(M):
            total = 0
            for d in range(5):
                row = delta_row[d]
                col = delta_col[d]
                # 중간값들 4번 더하는 애들
                if N-1> i > 0 and M-1> j > 0:
                    total += ballons[i+row][j+col]
                # 위 중간
                elif i == 0 and M-1 > j > 0:
                    if row != -1:
                        total += ballons[i+row][j+col]
                # 아래 중간T
                elif i == N-1 and M-1 > j > 0:
                    if row != 1:
                        total += ballons[i+row][j+col]
                # 왼쪽 중간
                elif 0 < i < N-1 and j == 0:
                    if col != -1:
                        total += ballons[i+row][j+col]
                elif 0 < i < N-1 and j == M-1:
                    if col != 1:
                        total += ballons[i+row][j+col]
                # 왼쪽위 꼭지점
                elif i == 0 and j == 0:
                    if row != -1 and col != -1:
                        total += ballons[i+row][j+col]
                # 왼쪽 아래 꼭지점
                elif i == N-1 and j == 0:
                    if row != 1 and col != -1:
                        total += ballons[i+row][j+col]
                # 오른쪽 위 꼭지점
                elif i == 0 and j == M-1:
                    if row != -1 and col != 1:
                        total += ballons[i+row][j+col]
                # 오른쪽 아래 꼭지점
                elif i == N-1 and j == M-1:
                    if row != 1 and col != 1:
                        total += ballons[i+row][j+col]
            flowerLst.append(total)
    print(flowerLst)
