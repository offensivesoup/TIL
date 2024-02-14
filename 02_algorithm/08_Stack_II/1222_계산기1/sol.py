import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1,T+1):
    stack = []
    N = int(input())
    fx = list(input())
    for i in range(N):
        if i % 2 == 1:
            fx[i], fx[i+1] = fx[i+1], fx[i]
        if i % 2 == 0:
            pass
    for tk in fx:
        if tk != '+':
            stack.append(int(tk))
        else:
            A = stack.pop()
            B = stack.pop()
            stack.append(A+B)
    print(f'#{tc} {stack[0]}')


