import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs(start):
    visited[start] = 1
    while que:
        cango = que.popleft()
        for s in city[cango]:
            if visited[s]:
                continue
            visited[s] = visited[cango] + 1 # 거리 표시
            que.append(s)
        # 백트래킹
        if visited[cango] == final + 1:
            break
    return



V, E, final, start = map(int,input().split())
city = [[] for _ in range(V+1)] # 그래프 만들어줌
visited = [0] * (V+1) # 방문표시할 리스트 만들어줌
for _ in range(E):
    left, right = map(int,input().split())
    city[left].append(right)
# 도시의 정보가 담겼다 1에서 2, 3으로 갈수있고, 2에서 3,4로 간다.
# 그런데 3은 이미 1에서 방문했으니까, 방문하지 않는다
que = deque([start])
bfs(start)
result = []
for i in range(V+1):
    if visited[i] == final + 1:
       result.append(i)
result.sort()
if result:
    for j in result:
        print(j)
else:
    print(-1)