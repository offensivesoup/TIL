'''
동생과 숨바꼭질
수빈이가 현재 점 N에 있고, 동생은 점 K
수빈이는 걷거나 순간이동 가능, 수빈이의 위치가 X 일때 1초 후에 X-1 or X+1
순간이동하면 2 * X 위치로
수빈이가 동생을 찾을 수 있는 가장 빠른 시간
K, N
'''
from collections import deque

def bfs(subin, goal):
    
    global mini
    while subin:
        point = subin.popleft()
        now = point[0]
        if now > 100000:
            continue
        time = point[1]
        if now > goal:
            if mini > time + (now - goal):
                mini = time + (now - goal)
            continue
        if now < 0:
            continue
        if now == goal:
            if mini > time:
                mini = time
                break
        if visited[now] == 1:
            continue
        visited[now] = 1
        subin.append((now - 1, time + 1))
        subin.append((now + 1, time + 1))
        subin.append((now * 2, time + 1))
            
        
N, K = map(int,input().split())
mini = 1e9
que = deque([(N,0)])
visited = [0] * 100001
bfs(que, K)
print(mini)

