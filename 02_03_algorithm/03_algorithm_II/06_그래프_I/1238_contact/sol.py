import sys
sys.stdin = open('input.txt')

from collections import deque

def bfs(start):
    que = deque([start])  # 큐에 시작값을 담는다
    while que:
        caller = que.popleft() # 전화를 건사람
        for call in calling[caller]:  # 그 리스트를 돌려서
            if not visited[call]:
                visited[call] += visited[caller] + 1  # 전화를 받았다고 표시해
                que.append(call)  # 전화를 받은 사람 목록을 만들어 줍니다

    return visited
for test_case in range(1,11):
    N, start = map(int,input().split()) # 데이터의 길이와 시작점
    siren    = list(map(int,input().split())) # from to from to 식으로 표시
    ## 동일한 쌍이 여러번 반복될 수도 있다. => 차이는 없음
    calling = [[] for _ in range(101)] # 비상 연락망
    visited = [0] * 101 # 전화 걸었는지 표시할거
    for i in range(0,N,2): # 누가 누구한테 전화거는지 보여줌
        calling[siren[i]].append(siren[i+1])
    bfs(start)
    maxi = max(visited)
    result = []
    for i in range(101):
        if visited[i] == maxi:
            result.append(i)
    print(max(result))
