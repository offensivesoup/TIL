# def BFS(G,v):
#     visited = [0] * (n+1) # 정점의 개수
#     queue   = [] # 큐 생성
#     queue.append(v) # 시작점 v를 큐에 삽입
#     while queue:
#         t = queue.pop(0)
#         if not visited[t]:
#             visited[t] = True
#             visit(t)
#             for i in G[t]:
#                 if not visited[i]:
#                     queue.append(i)


## 순서 바꿔서 진행 => Empty 가 아닌 full 을 기준으로

def BFS(G, v, n): # 그래프 G, 시작점 v
    visited = [0] * (n+1)
    queue   = []
    queue.append(v)
    visited[v] = 1
    while queue:
        t = queue.pop(0)
        visited(t)
        for i in G[t]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1

