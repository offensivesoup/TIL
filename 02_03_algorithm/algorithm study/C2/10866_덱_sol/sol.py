import sys
sys.stdin = open('input.txt')

from collections import deque

N = int(input())
commends = [input() for _ in range(N)]

deq = deque([])

for commend in commends:
    if commend[:2] == "pu":
        num = int(commend.split()[1])
        if commend[5] == "b":
            deq.append(num)
        else:
            deq.appendleft(num)
    elif commend[:2] == "po":
        if commend[4] == "f":
            if deq:
                print(deq.popleft())
            else:
                print(-1)
        if commend[4] == "b":
            if deq:
                print(deq.pop())
            else:
                print(-1)
    elif commend[0] == "s" :
        print(len(deq))
    elif commend[0] == "e":
        if deq:
            print(0)
        else:
            print(1)
    elif commend[0] == "f":
        if deq:
            print(deq[0])
        else:
            print(-1)
    else:
        if deq:
            print(deq[-1])
        else:
            print(-1)

            
