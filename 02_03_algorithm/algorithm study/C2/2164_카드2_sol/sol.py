'''
1 2 3 4 5 6
2 3 4 5 6
3 4 5 6 2
4 5 6 2
5 6 2 4
6 2 4
2 4 6
4 6
6 4
4
1 2 3 4
2 3 4
3 4 2
4 2
2 4
4
'''

from collections import deque

N = int(input())
que = deque(range(1,N+1))
while len(que) > 1:
    que.popleft()
    a = que.popleft()
    que.append(a)
print(que[0])
