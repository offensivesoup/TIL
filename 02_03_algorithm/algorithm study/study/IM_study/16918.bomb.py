'''
폭탄이 있는 칸은 3초 뒤에 폭발
터지면, 폭탄칸이 파괴 => 빈칸, 인접 4칸도 파괴(델타)
폭탄이 터졌는데, 폭탄이 있는 칸이 터지면 폭발 없이 터짐(연쇄x)
봄버맨의 행동강령
1. 봄버맨이 폭탄 설치함
2. 다음 1초 동안 아무것도 안함
3. 다음 1초 동안 폭탄 없는 칸에 폭탄을 설치한다. 동시설치
4. 1초가 지난뒤 1폭탄이 다 터진다.
5. 3과 4를 반복한다.
6. 0초 폭탄 1초 대기 2초 다음 폭탄 3초 펑, 4초 설치 5초 펑, 6초 설치, 7초 펑
'''

from collections import deque
from copy import deepcopy

R, C, N = map(int,input().split()) # R = 행 , C = 열, N = 몇초
# 0초의 상황(봄버맨이 폭탄을 설치해놓았다.)
area = [list(input()) for _ in range(R)]
watch = 1 # 1 초 부터 시작 (1초까지 암것도 안하니까)
# 델타 탐색
result = []
checkLst = []
delta_row = [-1,1,0,0]
delta_col = [0,0,-1,1]
que = deque()


# 동작 수행
while watch != N: # 시간이 다 가기 전까지
    for r in range(R):
        for c in range(C):
            if area[r][c] == 'O': # 폭탄이 설치된 곳이면
                que.appendleft([r,c]) # 해당 좌표값들을 que에 넣어놓는다.
            else: # 폭탄이 설치되지 않은 곳이면
                checkLst.append([r,c]) # 해당 좌표값들을 checkLst에 넣어놓는다.
    for check in checkLst:
        area[check[0]][check[1]] = 'O' # 설치 안된 곳에 설치한다.
    watch += 1 # 1초가 지났다.
    while que: # 터질 폭탄이 설치되어있으면
        bomb = que.popleft() # 큐에서 빼낸다.
        for d in range(4):
            row = bomb[0] + delta_row[d]
            col = bomb[1] + delta_col[d]
            if row > R - 1 or row < 0 or col > C - 1 or col < 0:
                continue
            else:
                area[row][col] = '.'
                area[bomb[0]][bomb[1]] = '.'
    watch += 1 # 1초가 다시 지난다.
    answer = deepcopy(area)
    result.append(answer)
    if watch == 5:
        break

# 출력하기
if N > 1:
    if N % 2 == 0:
        result = 'O' * C
        for i in range(R):
            print(result)
    elif N % 4 == 3:
        for r in result[0]:
            print(*r, sep = '')
    elif N % 4 == 1:
        for r in result[1]:
            print(*r, sep = '')
else:
    for r in area:
        print(*r, sep = '')



