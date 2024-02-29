import sys
sys.stdin = open('input.txt')

def check(arr):
    # 가로 세로 검증
    for i in range(9):
        row = [0] * 10
        col = [0] * 10
        for j in range(9):
            row_num = arr[i][j]
            col_num = arr[j][i]

            if row[row_num] : return 0
            row[row_num] = 1
            if col[col_num] : return 0
            col[col_num] = 1

    # 상자 검증
    for i in range(9):
        for j in range(9):
            if i % 3 == 0 and j % 3 == 0:
                square = [0] * 10
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        num = arr[r][c]
                        if square[num]: return 0
                        square[num] = 1

    return 1

T = int(input())

for test_case in range(1,T+1):
    area = [list(map(int,input().split())) for _ in range(9)] # 스도쿠 입력받기
    print(f'#{test_case} {check(area)}')