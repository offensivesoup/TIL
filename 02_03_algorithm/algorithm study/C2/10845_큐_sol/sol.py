import sys
sys.stdin = open('input.txt')

from collections import deque

N = int(input())
que = deque([])
commends = [input() for _ in range(N)]

for commend in commends:
    if commend[0] == "p":
        if commend[1] == 'u':
            que.append(int(commend.split()[1]))
        else:
            if que:
                print(que.popleft())
            else:
                print(-1)
    elif commend[0] == "s":
        print(len(que))
    elif commend[0] == "e":
        if que:
            print(0)
        else:
            print(1)
    elif commend[0] == "f":
        if que:
            print(que[0])
        else:
            print(-1)
    else:
        if que:
            print(que[-1])
        else:
            print(-1)

            