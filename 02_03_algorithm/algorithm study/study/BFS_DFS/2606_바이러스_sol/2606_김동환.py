import sys
sys.stdin = open('input.txt')
from collections import deque
'''
웜바이러스에 걸리면, 나머지 연결된 컴퓨터도 다걸림
연결된 컴퓨터가 다 걸린다고 가정
어느날 1번 컴퓨터가 바이러스에 걸리고
웜바이러스에 걸리게 되는 컴퓨터 수를 출력하시오
'''

def dfs(start, visited):
    global result
    visited[start] = 1
    for i in arr[start]:
        if not visited[i]:
            result += 1
            dfs(i, visited)

computers = int(input())
total = int(input())
visited = [0] * (computers + 1)
result = 0
arr = [[] for _ in range(computers+1)]
for i in range(total):
    idx, value = map(int,input().split())
    arr[idx].append(value)
    arr[value].append(idx)
visited[1] = 1
print(arr)
dfs(1, visited)
print(result)