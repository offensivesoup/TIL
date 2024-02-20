import sys
sys.stdin = open('input.txt')

# T = int(input())
#
# def result(k):
#     global cnt
#     cnt += 1
#
# def pre_order(now):
#     if now != 0:
#         result(now)
#         pre_order(tree[now][0])
#         pre_order(tree[now][1])
#
# for test_case in range(1,T+1):
#     E, N = map(int,input().split()) # E는 간선의 개수 N을 루트로 하는 서브 트리에 속한 노드의 개수
#     arr  = list(map(int,input().split())) # 입력받은 줄
#     tree = [[0,0] for _ in range(E+2)] # 트리 만들어줌
#     cnt = 0 # 결과
#     for idx in range(E): # 순회하여 트리에 채워줌
#         if tree[arr[idx*2]][0] != 0:
#             tree[arr[idx*2]][1] = arr[idx*2+1]
#         else:
#             tree[arr[idx*2]][0] = arr[idx*2+1]
#     pre_order(N) # 전위순회법으로 시작점을 입력해줌
#     print(f'#{test_case} {cnt}') # 결과 출력

## 강사님 코드

def pre_order(node):
    global result
    if node:
        result += 1
        pre_order(tree[node][0])
        pre_order(tree[node][1])


T = int(input())
for tc in range(1,T+1):
    E, N = map(int,input().split())
    tree = [[0,0] for _ in range(E+2)]
    lst = list(map(int,input().split()))
    for i in range(E):
        p = lst[i*2]
        c = lst[i*2+1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c

    result = 0 # N번 노드가 가지고 있는 자손 노드들의 수수
    pre_order(N)
    print(result)