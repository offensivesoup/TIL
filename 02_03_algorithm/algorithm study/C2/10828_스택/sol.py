import sys
sys.stdin = open('input.txt')

stack = []
N = int(input())
for _ in range(N):
    com = input()
    if com[:4] == 'push':
        stack.append(com[5:])
    elif com[:3] == 'pop':
        if stack:
            a = stack.pop()
            print(a)
        else:
            print(-1)
    elif com[:4] == 'size':
        print(len(stack))
    elif com[:5] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif com[:3] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)

