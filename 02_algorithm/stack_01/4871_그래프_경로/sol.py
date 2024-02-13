import sys
sys.stdin = open('input.txt')

# V 개 이내의 노드
# E 개의 간선
# 경로가 있으면 1 없으면 0
def dfs(v):
    stack.append(v)
    if visited[v] == 0:
        visited[v] = 1
        for i in adj[v]:
            if visited[i] == 0:
                dfs(i)




T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())

    visited = [0] * (V + 1)
    adj = [[] for _ in range(V + 1)]

    for _ in range(E):
        a, b = map(int, input().split())
        adj[a].append(b)
    S, G = map(int, input().split())
    stack = []
    dfs(S)
    if G in stack:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')

# def dfs(S, G):
#     stack = [S]
#     while stack:
#         v = stack.pop()
#
#         if visited[v] == 0:
#             visited[v] = 1
#
#             for i in range(1, V+1):
#                 if graph[v][i] == 1 and visited[i] == 0:
#                     if i == G:
#                         return 1
#                     stack.append(i)
#     return 0
#
# T = int(input())
# for tc in range(1,T+1):
#     V, E = map(int,input().split())
#     visited = [0] * (V+1)
#     graph   = [[0 for _ in range(V+1)]for _ in range(V+1)]
#
#     for _ in range(E):
#         i, j = map(int,input().split())
#         graph[i][j] = 1
#
#     S, G = map(int,input().split())
#     print(f'#{tc} {dfs(S,G)}')
#     print(graph)
    
        