import sys
sys.stdin = open('input.txt')

T = int(input())

def f(i,k,s, visited):
    global min_v
    if i == k:
        if min_v > s:
            min_v = s
    elif s >= min_v:
        return
    else:
        for j in range(N):
            if not visited[j]:
                visited[j] = 1
                f(i + 1, k, s + arr[i][j], visited)
                visited[j] = 0

for test_case in range(1,T+1):
    min_v = 100
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [0] * N
    f(0,N,0, visited)
    print(f'#{test_case} {min_v}')
