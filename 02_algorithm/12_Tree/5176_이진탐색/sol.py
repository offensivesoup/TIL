import sys
sys.stdin = open('input.txt')

def total_tree(n): # 완전트리를 만들어 보겟음
    global node # 각 노드에 들어갈 값이다.
    if n <= N: # 들어간 값이, 총 노드의 개수보다 커져선 안된다.
        total_tree(n*2) # 왼쪽 노드인덱스는 오른쪽위 노드 인덱스 곱하기 2
        tree[n] = node # 그 값이 인덱스에 들어감
        node += 1 # 노드에 1더해줌 1부터 순서대로 더해지는 것이다
        total_tree(n*2+1) # 오른 노드 인덱스는 왼쪽위 곱하기 2 더하기 1

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    tree = [0] * (N+1)
    node = 1
    total_tree(1)

    print(f'#{test_case} {tree[1]} {tree[N//2]}')