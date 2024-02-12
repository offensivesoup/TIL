import sys
sys.stdin = open('input.txt')

def dfs(S, G):
    stack = [0] # 시작점
    while stack:
        now = stack.pop()
        if visited[now] == 0:
            visited[now] = 1
            for next in range(100, 0, -1):
                if visited[next] == 0 and adj[now][next] == 1:
                    stack.append(next)
                    if next == 99:
                        return 1
    return 0

for tc in range(1,11):
    T, N = map(int,input().split())
    arr = list(map(int,input().split()))
    visited = [0] * 101
    adj = [[0] * 101 for _ in range(101)]
    for idx in range(N):
        adj[arr[idx * 2]][arr[idx * 2 + 1]] = 1
    print(f'#{tc} {dfs(0,99)}')