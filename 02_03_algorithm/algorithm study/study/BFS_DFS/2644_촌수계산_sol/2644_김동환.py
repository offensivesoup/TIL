import sys
sys.stdin = open('input.txt')

def dfs(start, visited, goal, cnt):
    global result
    visited[start] = 1
    if start == goal:
        result = cnt
        return
    for i in arr[start]:
        if not visited[i]:
            dfs(i, visited, goal, cnt+1)

n = int(input())

a, b = map(int,input().split())

m = int(input())

arr = [[] for _ in range(n+1)]
visited = [0] * (n+1)
result = 0
for _ in range(m):
    bumo, jasik = map(int,input().split())
    arr[bumo].append(jasik)
    arr[jasik].append(bumo)
dfs(a, visited, b, 0)
if result == 0:
    print(-1)
else:
    print(result)