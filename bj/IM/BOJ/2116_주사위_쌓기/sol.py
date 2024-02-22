import sys
sys.stdin = open('input.txt')
from collections import deque
'''
천수가 정육면체 주사위를 쌓는다. ( 항상 양쪽 면의 합이 7이 되지 않는다 )
쌓기 규칙 : 
1. 서로 붙은 두개의 주사위는 아래 주사위의 윗면과 위 주사위의 아랫면 같아야함
2. 1번 주사위는 맘대로 놓을 수 있음
이렇게 쌓으면 사각기둥이 되는데 사각기둥의 옆면은 총 4면
이렇게 해서 어느 한면의 숫자의 합이 최대가 되도록 주사위를 쌓는다. -> 주사위를 위아래는 고정하고, 옆으로 돌릴 수 있음
한 옆면 숫자의 최대값을 구하는 프로그램을 작성해라
'''

def stack_dice(d):
    pass


N = int(input()) # 주사위의 개수
dices = [list(map(int,input().split())) for _ in range(N)] # A면은 F면, B면은 D면, C면은 E면과 마주보고 있음
# 주사위의 아래,윗면을 고르는 경우는 총 6가지가 있다 (1번 주사위를 총 6번 바꿀 수 있기 때문에)
del_dicing = [5,3,4,1,2,0] # 마주보는 면의 목록
new_dices = []
result = []

for tc in range(6): # 총 6가지 경우의 수(사실)
    t = dices[0][tc] # 각 경우의 수에 맞는 첫번째 주사위의 천장값
    b = dices[0][del_dicing[tc]] # 각 천장값에 대응하는 첫번째 바닥값
    for s in range(1,N): # 그 다음 주사위 부터 돌려보기
        for n in range(6): # 주사위 번호 모두 순회
            if s < N: # 인덱스 에러 처리
                if dices[s][del_dicing[n]] == t: # 그 주사위의 바닥값이 천장값과 같다면?
                    t = dices[s][n] # 그 주사위의 천장은 그 바닥과 대응하는 값과 같다
                    b = dices[s][del_dicing[n]] # 바닥값
                    print(t,b)
