T = 10
for test_case in range(1,T+1):
    N = int(input())
    area = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            