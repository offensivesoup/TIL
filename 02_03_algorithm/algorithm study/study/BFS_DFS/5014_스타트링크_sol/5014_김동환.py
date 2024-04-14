import sys
sys.stdin = open('input.txt')
from collections import deque

def bfs(que, goal):
    global mini
    while que:
        poping = que.popleft()
        now = poping[0]
        time = poping[1]
        if now == goal:
            if mini > time:
                mini = time
                break
        up = now + U
        down = now - D
        if up <= F:
            if not visited[up]:
                visited[up] = 1
                que.append((up, time + 1))
        if down > 0:
            if not visited[down]:
                visited[down] = 1
                que.append((down, time + 1))
        visited[now] = 1

F, S, G, U, D = map(int,input().split())
mini = 1e9
visited = [0] * (F+1)
que = deque([(S,0)])
bfs(que, G)
if mini == 1e9:
    print('use the stairs')
else:
    print(mini)
