import sys
sys.stdin = open('input.txt')
from pprint import pprint
'''
공연장에 다음과 같이 격자형으로 배치되어 있다
사람들이 번호표를 받음 => (1,1) 부터 돌아가며 비어있는 좌석에 시계방향으로 배정
위쪽, 오른쪽, 아래쪽, 왼쪽 다시 위쪽 ~ 순으로 반복
공연장의 크기인 C R 이 주어질 때, 대기 순서가 K인 관객에게 배정될 좌석번호 찾음
'''
# 위, 오른, 아래, 왼쪽 순으로 리스트 만들기
del_row = [0,1,0,-1]
del_col = [1,0,-1,0]
C, R = map(int,input().split()) # 가로 C, 세로 R
K = int(input()) # 관객번호 수
stage = [[0] * (C+1) for _ in range(R+1)] # 공연 무대
pan = 1
move, row, col  = 0, 1, 1
x, y = 0, 0
stage[row][col] = pan
if C * R < K:
    print(0)
else:
    while pan < K:
        x = row + del_row[move]
        y = col + del_col[move]
        if 0 <= x <= C and 0 < y <= R:
            if stage[y][x] == 0: # 아직 안갔으면
                pan += 1
                stage[y][x] = pan # 팬으로 줌
                row += del_row[move] # 그만큼 전진함
                col += del_col[move] # 그만큼 전진함
            else:
                move = (move+1) % 4
        else:
            move = (move + 1) % 4  # 무브를 돌림
    pprint(stage)
    print(x, y)


