## 1. 그래프를 코드로 표현

# - 연결 리스트 ?
#  - 몇 개 연결될지 잘 모름
#  - 그래프는 두개가 한정이 아니라 , 

# - 인접 행렬
#  - V * V 배열을 활용해서 표현
#  - 갈 수 없다면 0, 있다면 1(가중치) 을 저장

# - 장점
#  - 노드간의 연결 정보를 한 방에 확인 가능
#  - 행렬곱을 이용해서 탐색이 쉽게 가능하다.
#  - 간선이 많을수록 유리

# - 단점
#  - 노드 수가 커지면, 메모리가 낭비된다.
#  - 연결이 안된 것도 저장
#  - 노드 수 + 메모리 제한 반드시 확인할 것!
# [2000][2000] 정도만 해도 터진다.

# 특징 : 양방향 그래프는 중앙 우하단 대각선을 기준으로 대칭이다

# graph = [
#     [0, 1, 0, 1, 0], # 1번과 3번을 갈 수 있으니까
#     [1, 0, 1, 0, 1],
#     [1, 0, 0, 0, 0],
#     [1, 0, 0, 0, 1],
#     [0, 1, 0, 1, 0],
# ]

# - 인접 리스트 (조금 더 권장)
#  - V 개의 노드가 갈 수 있는 정보만 저장한 방식

# - 장점
#  - 메모리 사용량이 적다
#  - 탐색할 때 갈 수 있는 곳만 확인하기 때문에
#    시간적으로 효율적이라고 볼 수 있다.
# - 단점
#  - 특정 노드 간 연결 여부를 확인하는데 시간이 걸린다.
#  -

# graph = [
#     [1, 3],
#     [0, 2, 4],
#     [1],
#     [0, 4],
#     [1, 3]
# ]

# ## 2. 인접 행렬 DFS : 재귀

# graph = [
#     [0, 1, 0, 1, 0],
#     [1, 0, 1, 0, 1],
#     [1, 0, 0, 0, 0],
#     [1, 0, 0, 0, 1],
#     [0, 1, 0, 1, 0],
# ]

# visited = [0] * 5

# def dfs(now):
#     # 기저 조건
#     # 지금 문제에서는 없다
    
#     # 다음 재귀 호출 전
#     visited[now] = 1
#     print(now, end = ' ')
#     # dfs : 현재 노드에서 다른 노드들을 확인
#     # 다른 노드들 == 반복문
#     for to in range(5):
#         ## 갈 수 없다면 pass
#         if graph[now][to] == 0:
#             continue
#         ## 이미 방문했다면 pass
#         if visited[to]:
#             continue

#     # 돌아왔을 때 작업
#         # 다음 재귀 호출
#         dfs(to)

# dfs(0)

## 인접 리스트 DFS: 재귀

# graph = [
#     [1, 3],
#     [0, 2, 4],
#     [1],
#     [0, 4],
#     [1, 3]
# ]

# visited = [0] * 5
# path    = []

# def dfs(now):
#     # 인접리스트
#     # 차이점 1. 갈수 없는 곳 조건 필요없음
#     # 차이점 2. for 문 작성시 인덱스 사용 필요없다
#     for to in graph[now]:
#         if visited[to]:
#             continue

#         visited[to] = 1
#         path.append(to)
#         dfs(to)

# dfs(0)

## 3. 인접 행렬 BFS:

# graph = [
#     [0, 1, 0, 1, 0],
#     [1, 0, 1, 0, 1],
#     [1, 0, 0, 0, 0],
#     [1, 0, 0, 0, 1],
#     [0, 1, 0, 1, 0],
# ]

# visited = [0] * 5

# # 1. 갈 수 있는 곳 다 가기
# # 2. 방문 순서대로 다음 노드
# #     - 먼저 방문 -> 먼저 다음 노드
# #     FIFO => queue

# def bfs(start):

#     # 시작 노드를 큐에 추가 + 방문 표시
#     queue   = [start]
#     visited[start] = 1

#     while queue:
#         now = queue.pop(0)
#         print(now, end = ' ')

#         # 갈 수 있는 곳을 체크한다.
#         for to in range(5):
#             if graph[now][to] == 0:
#                 continue

#             if visited[to]:
#                 continue
            
#             visited[to] = 1
#             queue.append(to)

# bfs(0)

# graph = [
#     [1, 3],
#     [0, 2, 4],
#     [1],
#     [0, 4],
#     [1, 3]
# ]

# visited = [0] * 5
# path    = []

# def bfs(start):
#     queue = [start]
#     visited[start] = 1

#     while queue:
#         now = queue.pop(0)
#         print(now, end = ' ')

#         for to in graph[now]:
#             if visited[to] == 1:
#                 continue

#             visited[to] = 1
#             queue.append(to)

# bfs(0)

## 상호 배타 집합에 대한 연산

# 1~6번까지 노드가 존재.
# 1. make_set

def make_set(n):
    # 자기자신인 대표인 데이터가 리스트로 생성
    return [i for i in range(n)] # 숫자는 대표자의 인덱스이다.

# 1~6번 까지를 사용하기 위해 7개 생성(0번은 버림)
parents = make_set(7)

# 2. find_set : 대표자를 찾아보자
# - 부모 노드를 보고, 부모 노드도 연결이 되어있다면 다시 반복
# - 언제까지 ? 자기자신이 대표인 데이터를 찾을 때 까지
def find_set(x):
    if parents[x] == x: # 부모가 대표자 자기 자신이네?
        return x # 그럼 끝
    # 기저 조건에 안걸리면 == 대표자가 따로 있다
    return find_set(parents[x])

# 3. union
def union(x, y):
    x = find_set(x)
    y = find_set(y)
    # 이미 같은 집합에 속해있다면 continue
    if x == y:
        return
    
    # 다른 집합이라면 합침
    # 예 ) 더 작은 루트노드에 합쳐라 ~
    if x < y :
        parents[y] = x
    else:
        parents[x] = y

print(parents)
union(1,3)
print(parents)
union(2,3)
print(parents)
union(5,6)
print(parents)
