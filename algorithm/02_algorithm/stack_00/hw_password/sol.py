import sys
sys.stdin = open('input.txt')

T = 10

for test_case in range(1,T+1):
    NN, M = map(int,input().split())
    pw   = str(M)
    N = len(pw)
    stack = [None] * 100
    stack[0] = pw[0]
    top = 0
    result = ''
    total = 0
    for i in range(1,N):
        if stack[top] != pw[i]:
            top += 1
            stack[top] = pw[i]
        else:
            stack[top] = None
            top -= 1
    for num in stack:
        if num is not None:
            result += str(num)
        else:
            break
    print(f'#{test_case} {int(result)}')