import sys
sys.stdin = open('input.txt')
from pprint import pprint
T = int(input())

d_row = [-1,1,0,0]
d_col = [0,0,-1,1]

for tc in range(1,T+1):
    N = int(input())
    miro = [[int(x) for x in input()] for _ in range(N)] # 미로
    stack   = [] # 스택 생성
    result  = 0
    for i in range(N): # 시작점 담기
        for j in range(N):
            if miro[i][j] == 2:
                stack.append([i,j]) # 스택에 시작점을 담았어
                break
    while stack: # 스택이면
        point = stack.pop() # 지금 지점을 포인트로 찍을게
        for r in range(4): # 델타탐색
            row = point[0] + d_row[r]
            col = point[1] + d_col[r]
            if row >= N or row < 0 or col >= N or col < 0:  # 경계를 벗어나면 못가는 거야
                continue # 다음 탐색점으로 넘어가
            elif miro[row][col] == 0: # 통로였네?
                miro[row][col] = 1 # 간거임
                stack.append([row,col]) # 그 지점을 스택에 넣을 거임
            elif miro[row][col] == 3 : # 도착점이네?
                result = 1 # 도착했다고 표시
                break
    print(f'#{tc} {result}')




