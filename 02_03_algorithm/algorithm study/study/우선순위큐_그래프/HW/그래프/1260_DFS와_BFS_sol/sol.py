import sys
sys.stdin = open('input.txt')
from collections import defaultdict, deque

def bfs(start, visited, bfsResult):
    que = deque([start]) # start가 들어가 있는 덱
    visited[start] = 1 # 시작점은 찍어주고
    while que:
        start = que.popleft() # 젤 시작값 빼주고
        for s in edges[start]: # 그 간선들을 본다
            if visited[s]: # 만약 간적이 있다면
                continue # 다른걸 보고
            visited[s] = 1 # 방문표시 해주고
            bfsResult.append(s) # 결과값에 넣어주고
            que.append(s) # 큐에도 넣어준다

    return

def dfs(start, visited):
    visited[start] = 1
    dfsResult.append(start)
    for i in edges[start]:
        if not visited[i]:
            dfs(i, visited)

V, E, start = map(int,input().split())
# 정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호
edges = [[] for _ in range(V+1)]
# 연결 리스트 만들기
for _ in range(E):
    left, right = map(int,input().split()) # 좌우 값이 주어진다
    edges[left].append(right)
    edges[right].append(left)

for edge in edges:
    edge.sort()

visited = [0] * (V+1) # 방문 기록을 찍어줄거야
visited[start] = 1
dfsResult = [] # 결과를 만들어줄 리스트
stack = []
dfs(start, visited)
print(*dfsResult)

visited = [0] * (V+1) # 방문 기록을 찍어줄거야
bfsResult = [start] # 결과를 만들어줄 리스트
bfs(start, visited, bfsResult)
print(*bfsResult)