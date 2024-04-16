import sys
sys.stdin = open('input.txt')
from collections import deque

def acp_sort():
    global result
    que = deque([])
    for i in range(1, N + 1):
        if not indgree[i]:
            que.append(i)
    while que:
        now = que.popleft()
        result.append(now)
        for ac in acp[now]:
            indgree[ac] -= 1
            stair = []
            if not indgree[ac]:
                que.append(ac)
                stair.append(ac)

T = int(input())

for test_case in range(T):
    N, K = map(int,input().split()) # 건물의 개수, 건설 순서 규칙 (정점과 엣지)
    acp = [[] for _ in range(N+1)]
    indgree = [0] * (N+1)
    times = [0] + list(map(int,input().split()))
    result = []
    mini   = 1e9
    for i in range(1,K+1):
        x, y = map(int,input().split()) # x를 지어야 y를 지을 수 있다.
        acp[y].append(x)
        indgree[x] += 1
    goal = int(input())
    print(acp)
    acp_sort()
    print(result)