import sys
sys.stdin = open('input.txt')

T = 10
for test_case in range(1,T+1):
    N = int(input())
    area = [list(map(int,input().split())) for _ in range(N)]
    magnetics = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if area[j][i] != 0:
                magnetics[i].append(area[j][i])
    sumi = 0
    for n in range(N):
        stack = []
        for m in range(len(magnetics[n])):
            if magnetics[n][m] == 1:
                stack.append(1)
            else:
                if stack:
                    a = stack.pop(0)
                    if a == 1:
                        sumi += 1
                        stack.clear()
                    else:
                        pass
    print(f'#{test_case} {sumi}')






