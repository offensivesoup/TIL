import sys
sys.stdin = open('input.txt')

stack = []
N = int(input())
commend = [input() for _ in range(N)]
for com in commend:
    if com[0] == 'p':
        if com[1] == 'u': # push라면
            num = int(com[5:])
            stack.append(num)
            continue
        else: # pop이라면
            if stack:
                print(stack.pop())
            else:
                print(-1)
    elif com[0] == 's':
        print(len(stack))
    elif com[0] == 'e':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)


