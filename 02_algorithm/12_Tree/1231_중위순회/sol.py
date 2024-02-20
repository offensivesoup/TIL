import sys
sys.stdin = open('input.txt')

# T = 10
#
# def result(word):
#     print(check[word-1][1], end = '')
#
# def in_order(now):
#     if now != 0:
#         in_order(tree[now][0])
#         result(now)
#         in_order(tree[now][1])
#
# for test_case in range(1,T+1):
#     N = int(input()) # 노드의 개수
#     tree = [[0,0] for _ in range(N+1)]
#     check = [[0,0,0,0] for _ in range(N)]
#     user_input = [list(input().split()) for _ in range(N)]
#     for k in range(N):
#         for l in range(len(user_input[k])):
#             check[k][l] = user_input[k][l]
#
#     for i in range(N):
#             left = int(check[i][2])
#             right = int(check[i][3])
#             if left != 0:
#                 tree[i+1][0] = left
#             if right != 0:
#                 tree[i+1][1] = right
#     print(f'#{test_case}', end = ' ')
#     in_order(1)
#     print()

## 강사님 코드

def inorder(node):
    if node:
        inorder(int(tree[node][2]))
        print(tree[node][1], end = '')
        inorder(int(tree[node][3]))

for tc in range(1,11):
    N = int(input())
    # 노드번호, 값, 왼쪽, 오른쪽자식
    # 자식이 없을 수 있음
    tree = [input().split() for _ in range(N)]
    tree.insert(0,['0','0','0','0'])
    for node in tree: # 모든 노드 순회
        while len(node) != 4: # 없는 자식 정보가 누락되었다면
            node.append('0') # 없는 자식 정보를 삽입한다.
    print(f'#{tc}', end = ' ')
    inorder(1)
    print()