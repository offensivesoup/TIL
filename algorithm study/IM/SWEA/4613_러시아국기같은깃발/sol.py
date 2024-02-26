import sys
sys.stdin = open('input.txt')

T = int(input())
'''
깃발을 만들 수 있는 경우의 수
고로 최소값은, 모든 경우의 수를 비교해볼 수 있다.
그런데 각각 적어도 첫줄은 흰줄이고
마지막 줄은 빨간줄이다.
그럼 해당값을 먼저 고정시켜놓자.
고정 후 다음 순서로 진행시켜볼 수 있을 것같다
맨 바닥을 빨강, 맨 위를 하양 나머지 다 파랑 을 반복
4가지 경우의 수가 있는것이다
맨 바닥이랑 맨 천장 빼고 나머지 부분에서
1. 맨 위는 하양 나머지는 파랑
2. 맨 밑은 빨강 나머지는 파랑
3. 그냥 다 파랑
4. 맨 위는 하양 맨 밑은 빨강 나머지 파랑
이렇게 4가지 씩 다 넣어보는 거임 리스트에
'''
for test_case in range(1,T+1):
    N, M = map(int,input().split())
    flag = [list(input()) for _ in range(N)]
    start = 0 # 시작값
    for i in range(N):
        for j in range(M):
            if i == 0: # 첫번째 줄인데,
                if flag[i][j] != 'W': # 흰색이 아님
                    start += 1
            elif i == N-1: # 마지막 줄인데,
                if flag[i][j] != 'R': # 빨간색이 아님
                    start += 1
    rear = N-1 # 바닥
    front = 1 # 천장
    totalLst = []
    for s in range(3):
        if s == 0:
            next = start
