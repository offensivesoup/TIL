import sys
sys.stdin = open('input.txt')

from heapq import heappush, heappop, heapify
import collections

def prim(graph, start):
    visited[start] = 1
    candidate = graph[start] # 인접 간선 추출
    heapify(candidate) # 우선순위 큐 생성
    sumi = 0
    while candidate:
        w, s, e = heappop(candidate)
        if visited[e] == 0:
            visited[e] = 1
            sumi += w
            for edge in graph[e]:
                if visited[edge[2]] == 0:
                    heappush(candidate, edge)
    return sumi

T = int(input())

for test_case in range(1,T+1):
    V, E = map(int,input().split())
    graph = collections.defaultdict(list)
    visited = [0] * (V+1)
    for _ in range(E):
        s, e, w = map(int,input().split())
        graph[s].append([w,s,e])
        graph[e].append([w,e,s])
    # print(graph)

    print(f'#{test_case} {prim(graph,0)}')

    

        