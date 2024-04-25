import sys
sys.stdin = open('input.txt')
import heapq
import collections

'''
0-1-2-3-4-5-6 이 가장 최소의 비용으로 연결되어야 한다!
'''
def prim(graph, start_node):
    visited[start_node] = 1
    candidate = graph[start_node]
    heapq.heapify(candidate)
    total_weight = 0
    while candidate:
        weight, u, v = heapq.heappop(candidate)
        if visited[v] == 0:
            visited[v] = 1
            total_weight += weight
            for edge in graph[v]:
                if visited[edge[2]] == 0:
                    heapq.heappush(candidate, edge)
    return total_weight

while True:
    m, n = map(int,input().split()) # m은 집의 수 n 은 길의 수
    if m == n == 0:
        break
    visited = [0] * (n+1)
    graph = collections.defaultdict(list)
    sumi = 0
    for _ in range(n):
        x, y, z = map(int,input().split()) # 양 집과 그 거리 정보(가중치: 짧을수록 좋다)
        graph[x].append([z,x,y])
        graph[y].append([z,y,x])
        sumi += z
    print('요게 만들어진 그래프 : ' , graph)
    print('요게 프림한 결과 : ', prim(graph,0))
    print('프림한뒤 그래프 : ', graph)



    


