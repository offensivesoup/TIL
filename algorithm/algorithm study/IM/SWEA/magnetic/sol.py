T = 10
for test_case in range(1,T+1):
    N = int(input())
    area = [list(map(int,input().split())) for _ in range(N)]
    stack = []
    for i in range(N):
        for j in range(N):
            if not stack: # 텅 비었는데
                if area[j][i] == 1: # N극이면
                    pass # 그냥 사라짐
                elif area[j][i]
            a = stack.pop()
