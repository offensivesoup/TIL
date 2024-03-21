# ## prim

# '''
# 7 11
# 0 1 32
# 0 2 31
# 0 5 60
# 0 6 51
# 1 2 21
# 2 4 46
# 2 6 25
# 3 4 34
# 3 5 18
# 4 5 40
# 4 6 51
# '''

# from heapq import heappop, heappush

# def prim(start):
#     pq  = []
#     MST = [0] * V

#     # 최소 비용
#     sum_weight = 0

#     # 시작점 추가
#     # [기존 BFS] 노드 번호만 관리
#     # [PRIM] 가중치가 낮으면 먼저 나와야 한다.
#     # -> 관리해야할 데이터 : 가중치, 노드번호 2가지
#     # -> 동시에 두가지 데이터 다루기
#     #   1. class 로 만들기
#     #   2. 튜플로 관리
#     # 이차원 배열 + 가중치 + 높이
#     heappush(pq, (0, start))
#     while pq:
#         weight, now = heappop(pq)
#         ## 방문 했다면 continue
#         if MST[now]:
#             continue
#         ## 방문 처리
#         MST[now] = 1
#         # 누적합 추가
#         sum_weight += weight
#         # 갈 수 있는 노드들을 보면서
#         for to in range(V):
#             # 갈 수 없거나 이미 방무했다면 pass
#             if graph[now][to] == 0 or MST[to]:
#                 continue
#             heappush(pq, (graph[now][to], to))

#     print(f'최소 비용 : {sum_weight}')


# V, E = map(int, input().split())
# # 인접 행렬로 저장
# # - [과제] 인접 리스트로 저장

# graph = [[0] * V for _ in range(V)]
# for _ in range(E):
#     s, e, w = map(int,input().split())
#     # 기존 3 -> 4로 갈 수 있다.
#     graph[3][4] = 1
#     graph[s][e] = w
#     graph[e][s] = w # 무방향 그래프

# print(graph)


# # [기존] 3 -> 4로 갈 수 있다.
# graph[3][4] = 1

# # 가중치 그래프
# graph[3][4] = 31
# "3 -> 4 로 가는 데 31이라는 비용이 든다"
# prim(0)






# ## Kruskal

# # 1. 전체 그래프를 보고, 가중치가 제일 작은 간선부터 뽑자
# # -> 코드로 구현 : 전체 간선 정보를 저장 + 가중치로 정렬

# # 2. 방문처리
# # -> 이 때, 싸이클이 발생하면 안된다!
# # -> 싸이클 여부 ?? ==> union-find 알고리즘이 활용

# def union(x, y):
#     x = find_set(x)
#     y = find_set(y)

#     # 같은 집합이면 pass
#     if x == y:
#         return
    
#     if x < y:
#         parents[y] = x
#     else:
#         parents[x] = y


# def find_set(x):
#     if parents[x] == x:
#         return x
    
#     # 경로 압축
#     parents[x] = find_set(parents[x])
#     return parents[x]

# V, E = map(int,input().split())
# edges = [] # 간선 정보들을 모두 저장
# for _ in range(E):
#     s, e, w = map(int,input().split())
#     edges.append([s, e, w])
# edges.sort(key = lambda x : x[2]) # 가중치를 기준으로 정렬
# parents = [i for i in range(V)]   # 대표자 배열 (자기 자신을 바라봄)

# ## MST 완성 = r간선의 개수 V- 1
# sum_weight = 0

# # 간선들을 모두 확인한다.
# cnt = 0
# for s, e, w in edges:
#     # 싸이클이 발생하면 pass
#     # -> 이미 같은 집합에 속해 있다면 pass
#     if find_set(s) == find_set(e):
#         print(s, e, w,'싸이클 발생 탈락')
#         continue
#     # 대표자가 같다 !! = 연결되어있다
#     print(s, e)
#     cnt += 1
#     # 싸이클이 없다면, 방문 처리
#     union(s, e)
#     sum_weight += w

#     if cnt == V-1:
#         break

# print(f'최소비용 = {sum_weight}')


from heapq import heappush, heappop
## dijkstra

'''
6 8
0 1 2
0 2 4
1 2 1
1 3 7
2 4 3
3 4 2
3 5 1
4 5 5
'''

INF = int(1e9)

V, E = map(int,input().split())
start = 0 # 시작 노드 번호

# 인접리스트
graph = [[] for _ in range(V)]
# 누적거리를 저장할 변수
distance = [INF] * V

# 간선 정보 저장
for _ in range(E):
    s, e, w = map(int,input().split())
    graph[s].append([e,w])

def dijkstra(start):
    pq = []
    # 시작점의 weight, node 번호를 한 번에 저장
    heappush(pq, (0,start))
    # 시작 노드 초기화
    distance[start] = 0

    while pq:
        # 최단 거리 노드에 대한 정보
        dist, now = heappop(pq)
        # now 에서 인접한 다른 노드 확인
        for to in graph[now]:
            next_dist = to[0]
            next_node = to[1]

            new_dist =



