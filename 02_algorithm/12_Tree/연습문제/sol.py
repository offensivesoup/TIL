import sys
sys.stdin = open('input.txt')

## 온라인 코드

# def pre_order(T):
#     if T:
#         print(T, end = ' ')
#         pre_order(left[T])
#         pre_order(right[T])
#
# N = int(input()) # 1번부터 N번까지인 정점
# E = N-1
# arr = list(map(int,input().split()))
# left = [0] * (N+1) # 부모를 인덱스로 왼쪽자식번호 저장
# right = [0] * (N+1) # 오른쪽 자식
# par  = [0] * (N+1)  # 자식을 인덱스로 부모 저장
# for i in range(E):
#     p, c = arr[i*2], arr[i*2+1]
# # for i in arr[i], arr[i+1]:
# #     p, c = arr[i], arr[i+1] 이렇게도 할 수 있다.
#     if left[p] == 0: #왼쪽자식 이 없으면
#         left[p] = c
#     else:
#         right[p] = c
#     par[c] = p
#
# c = N
# while par[c] != 0: # 부모가 있으면
#     c = par[c] # 부모를 새로운 자식으로 해서
# root = c  # 더 이상 부모가 없으면 root
# print(root)
#
# c = N
# while par[c] != 0:
#     c = par[c]
# root = c
# pre_order(root)
# # print(root)


## 오프라인 코드

def solution(k): # 할일이 노드번호를 출력하는 것,
    print(k, end = ' ')

def preorder(now): # 조사 시작 노드 번호부터 조사를 시작한다.
    # 노드 번호 0은 없음
    # 따라서 노드 번호가 0 이 아닌 경우만 조사할 수 있어야함
    # 전위 순회는, 조사 시작 노드 번호에 대해서 할 일을 수행
    if now != 0:
        solution(now) # 현재 노드 번호에 대해 할일 수행
        # 왼쪽 자식 순회
        preorder(tree[now][0])
        # 오른쪽 자식 순회
        preorder(tree[now][1])

def inorder(now):
    if now != 0:
        inorder(tree[now][0])
        solution(now)
        inorder(tree[now][1])

def postorder(now):
    if now != 0:
        postorder(tree[now][0])
        postorder(tree[now][1])
        solution(now)




V = int(input())
edge = list(map(int,input().split()))
print(edge)
E = len(edge)

## tree[현재 노드 번호][0] => 현재 노드 번호의 왼쪽 자식 노드 번호
tree = [[0,0] for _ in range(V+1)]
for idx in range(E//2):
    # 특정 위치에 값을 할당하는 것.
    if tree[edge[idx*2]][0] == 0: # 왼쪽 자식의 정보가 아직 없다면
        # 왼쪽 자식에 자식 정보 삽입
        tree[edge[idx*2]][0] = edge[idx*2+1]
    else:
        # 왼쪽 자식이 이미 있다면 오른쪽에 자식 정보 삽입
        tree[edge[idx * 2]][1] = edge[idx*2+1]

print(tree)

preorder(1)
print()
inorder(1)
print()
postorder(1)
## 인접 리스트
# adj = [[] for _ in range(V+1)] # 0번 노드는 없다
# print(adj)
#
# for idx in range(E//2):
#     adj[edge[idx*2]].append(edge[idx*2+1])
# print(adj)

