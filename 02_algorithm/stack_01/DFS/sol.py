import sys
sys.stdin = open('input.txt')

def DFS(start):
    stack = [start] # 다음 조사 대상
    while stack:    # 조사 대상이 없어질때까지
        now = stack.pop()   # LIFO
        if visited[now] == 0:
            visited[now] = 1 # 방문 표시
            print(now, end = ' ')
        # 다음번 조사 대상이 누구냐 -> 인접리스트 adj[now]대상 모두 조사
            for next in range(V, 0, -1): # 0번 노드 제외한 모든 노드 번호 now에서 이동가능한지 판별
                if visited[next] == 0 and adj[now][next] == 1:
                    stack.append(next)
V, E = map(int,input().split())
arr  = list(map(int,input().split()))
visited = [0] * (V+1) # 0번 노드 없음.
## 인접행렬이라는 것을 만들어 보자
## 경로를 2차원 행렬로 만들어 낼 수 있다.
adj = [[0] * (V+1) for _ in range(V + 1)]
for idx in range(E):
    adj[arr[idx * 2]][arr[idx * 2 + 1]] = 1
    adj[arr[idx * 2 + 1]][arr[idx * 2]] = 1

for i in range(V + 1):
    print(adj[i])

DFS(1)



# adj = [[] for _ in range(V+1)]
# for idx in range(E):
#     # 2번방식
#     adj[arr[idx*2]].append(arr[idx*2+1])
#     adj[arr[idx * 2 + 1]].append(arr[idx * 2])

# 1번방식
# for idx in range(0, E * 2, 2): # 간선의 개수는 개당 2개의 노드 번호 가짐
    # from_node = arr[idx]
    # to_node   = arr[idx+1]
    # adj[from_node].append(to_node)
    # adj[to_node].append(from_node)