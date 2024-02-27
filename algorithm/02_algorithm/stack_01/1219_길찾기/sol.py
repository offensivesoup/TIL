import sys
sys.stdin = open('input.txt')

def dfs(S, G):
    stack = [S] # 시작점
    while stack:
        now = stack.pop() # 지금 지점을 찍을 거임
        if visited[now] == S:
            visited[now] = 1 # 방문 했다고 남김
            for next in range(100, 0, -1): # 거꾸로 가봄
                if visited[next] == 0 and adj[now][next] == 1:
                    stack.append(next) # 만약 안가봣고 가야하면 스택에 넣음
                    if next == G: # 99에 도착
                        return 1 # 결과리턴함
    return 0

for tc in range(1,11): # 테스트케이스 실행
    T, N = map(int,input().split())
    arr = list(map(int,input().split()))
    visited = [0] * 101
    adj = [[0] * 101 for _ in range(101)]
    for idx in range(N):
        adj[arr[idx * 2]][arr[idx * 2 + 1]] = 1 # 방향 이니까 하나만 넣어줌
    print(f'#{tc} {dfs(0,99)}')