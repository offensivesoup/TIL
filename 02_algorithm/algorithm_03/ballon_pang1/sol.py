import sys
sys.stdin = open('input.txt')
'''
if ni in range(N) and nj in range(M):
flowers += balloons[ni][nj]
'''
T = int(input())
for test_case in range(1, T+1):
    N, M = map(int,input().split())
    ballons = [list(map(int,input().split())) for _ in range(N)]
    flowerLst = []
    ballonLst = []
    for i in range(0,N):
        for j in range(0,M):
            total = 0 # 다 더해줄 값
            deltaLst = []
            for delta in range(-ballons[i][j], ballons[i][j] + 1):
                if delta != 0:
                    deltaLst.append(delta)
            total += ballons[i][j] # 일단 자기꺼 터트림
            for k in range(len(deltaLst)):
                if deltaLst[k] < 0: #왼쪽이나 아래로 가야한다면
                    # 열이 내가 터질꺼 보다 오른쪽에 있다면
                    if j + deltaLst[k] >= 0:
                        total += ballons[i][j+deltaLst[k]] # 왼쪽으로 갈 수 있음
                    # 행이 내가 터질꺼 보다 아래에 있다면
                    if i + deltaLst[k] >= 0:
                        total += ballons[i+deltaLst[k]][j] # 아래로 갈 수 있음
                elif deltaLst[k] > 0: #오른쪽이나 위로
                    # 열이 내가 터질꺼 보다 왼쪽에 있다면
                    if j + deltaLst[k] < M:
                        total += ballons[i][j + deltaLst[k]]  # 왼쪽으로 갈 수 있음
                    # 행이 내가 터질꺼 보다 위에 있다면
                    if i + deltaLst[k] <= N-1:
                        total += ballons[i + deltaLst[k]][j]  # 위로로 갈 수 있음
            ballonLst.append(total)
    print(f'#{test_case} {max(ballonLst)}')

            # T = int(input())
            # for test_case in range(1, T+1):
            #     N, M = map(int,input().split())
            #     ballons = [list(map(int,input().split())) for _ in range(N)]
            #     flowerLst = []
            #     for i in range(N):
            #         for j in range(M):
            #             total = 0
            #             for d in range(5):
            #                 row = ballons[i][j]
            #                 col = ballons[i][j]
            #                 # 중간값들
            #                 if N-1> i > 0 and M-1> j > 0:
            #                     total += (ballons[i+row][j+col] + ballons[i-row][i+col] + ballons[i+row][i-col] + ballons[i-row][i-col])
            #                 # 위 중간
            #                 elif i == 0 and M-1 > j > 0:
            #                     if row != -1:
            #                         total += (ballons[i+row][j+col] + ballons[i-row][i+col] + ballons[i+row][i-col] + ballons[i-row][i-col])
            #                 # 아래 중간
            #                 elif i == N-1 and M-1 > j > 0:
            #                     if row != 1:
            #                         total += (ballons[i+row][j+col] + ballons[i-row][i+col] + ballons[i+row][i-col] + ballons[i-row][i-col])
            #                 # 왼쪽 중간
            #                 elif 0 < i < N-1 and j == 0:
            #                     if col != -1:
            #                         total += (ballons[i+row][j+col] + ballons[i-row][i+col] + ballons[i+row][i-col] + ballons[i-row][i-col])
            #                 elif 0 < i < N-1 and j == M-1:
            #                     if col != 1:
            #                         total += (ballons[i+row][j+col] + ballons[i-row][i+col] + ballons[i+row][i-col] + ballons[i-row][i-col])
            #                 # 왼쪽위 꼭지점
            #                 elif i == 0 and j == 0:
            #                     if row != -1 and col != -1:
            #                         total += (ballons[i+row][j+col] + ballons[i-row][i+col] + ballons[i+row][i-col] + ballons[i-row][i-col])
            #                 # 왼쪽 아래 꼭지점
            #                 elif i == N-1 and j == 0:
            #                     if row != 1 and col != -1:
            #                         total += (ballons[i+row][j+col] + ballons[i-row][i+col] + ballons[i+row][i-col] + ballons[i-row][i-col])
            #                 # 오른쪽 위 꼭지점
            #                 elif i == 0 and j == M-1:
            #                     if row != -1 and col != 1:
            #                         total += (ballons[i+row][j+col] + ballons[i-row][i+col] + ballons[i+row][i-col] + ballons[i-row][i-col])
            #                 # 오른쪽 아래 꼭지점
            #                 elif i == N-1 and j == M-1:
            #                     if row != 1 and col != 1:
            #                         total += (ballons[i+row][j+col] + ballons[i-row][i+col] + ballons[i+row][i-col] + ballons[i-row][i-col])
            #                 flowerLst.append(total)

            # for k in range(4):
            #     if j >= 1 and j < M-1: # 젤 중간값들
            #         total += ballons[i+delta_row[k]][j+delta_col[k]] # 사방이 터짐 (최소1)
            #         while True: # 더 터질게 남아있지 않을 때 까지
            #             total += ballons[i+delta_row[k] + addB][j+delta_col[k] + addB]
            #             ballons[i][j] -= 1
            #             if ballons[i][j] == 1:
            #                 break
            #             # elif
            #     elif j == 0:# 왼쪽 값들 (col = -1인 경우를 제외)
            #         if k != 2:
            #             total += ballons[i+delta_row[k]][j+delta_col[k]]
            #     else: # 오른쪽 끝값들 (col = +1인 경우를 제외)
            #         if k != 3:
            #             total += ballons[i+delta_row[k]][j+delta_col[k]]




