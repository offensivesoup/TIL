import sys
sys.stdin = open('input.txt')

T = 10

def post_order(v):
    if v:
        post_order(int(left[v]))
        post_order(int(right[v]))
        if tree[v] == '+':
            tree[v] = int(tree[int(left[v])]) + int(tree[int(right[v])])
        elif tree[v] == '-':
            tree[v] = int(tree[int(left[v])]) - int(tree[int(right[v])])
        elif tree[v] == '*':
            tree[v] = int(tree[int(left[v])]) * int(tree[int(right[v])])
        elif tree[v] == '/':
            tree[v] = int(tree[int(left[v])]) // int(tree[int(right[v])])
    return

for test_case in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)

    for i in range(N):
        user_input = input().split()
        tree[i+1] = user_input[1]
        if user_input[1] in "+/*-":
            left[i+1] = user_input[2]
            right[i+1] = user_input[3]
    post_order(1)
    print(f'#{test_case} {tree[1]}')

## eval 을 사용할 수도 있다.

