import sys
sys.stdin = open('input.txt')

T = int(input())
stone_row = [-2,2,0,0,-2,-2,2,2]
stone_col = [0,0,-2,2,2,-2,2,-2] # 다른 돌을 탐색하기 위함

for test_case in range(1,T+1):
    N, M = map(int,input().split())
    area = [[0 for _ in range(N)] for _ in range(N)]
    p = N // 2
    area[p-1][p-1], area[p][p] = 2, 2 # 백돌
    area[p-1][p], area[p][p-1] = 1, 1 # 흑돌
    stack = []
    for _ in range(M): # 정해진 횟수만큼 돌을 놓는데
        x, y, stone = map(int,input().split()) # 정보 입력
        x -= 1
        y -= 1
        area[x][y] = stone
        # 그런데 그 사이 돌이 자기 돌로 바뀌어야함
        for i in range(8):
            row = x + stone_row[i] # 탐색돌
            col = y + stone_col[i] # 탐색돌
            if row >= N or row < 0 or col >= N or col < 0:
                continue
            else:
                if area[row][col] != stone and area[row][col] != 0: # 빈공간이나, 같은 돌이 아니라면
                    change_row = x + (stone_row[i] // 2)  # 바뀔 위치
                    change_col = y + (stone_col[i] // 2)  # 바뀔 위치
                    area[change_row][change_col] = stone # 그 사이돌 내걸로 바꿈
    print(area)