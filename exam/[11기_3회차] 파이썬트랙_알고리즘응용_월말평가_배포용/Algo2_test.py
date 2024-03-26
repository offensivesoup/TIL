import sys
sys.stdin = open('algo2_sample_in.txt')

T = int(input())

def build(bridge):
    ## 만약 부분집합이
    ## 만들수 있는 최대다리수를 예산 초과없이 만들 수 있다면
    ## 결과에 나타낸다
    for sub in subsets:
        sumi = sum(sub) # 다리 만드는 총 비용
        if len(sub) == bridge: # 다리의 개수가 같다면
            if sumi < budget: # 예산을 초과하지 않는다면
                result.append((bridge, sumi)) # 결과에 더해주고
    if result: # 만약 만들어진 결과가있으면
        result.sort(key = lambda x : x[1]) # 예산순으로 정렬하여
        return # 멈춘다
    build(bridge - 1) # 없으면, 하나 적개 만드는 경우를 고려하여 재귀한다.

for test_case in range(1, T+1):
    island, budget = map(int,input().split()) # 섬의 수와 예산
    result = []
    cost = list(map(int,input().split())) # 다리 각각에 대한 건설 비용
    maxi = island # 원래 다리는 섬의 개수만큼 지을 수 있는 것이 베스트이다.
    mini = 1e9
    ## 먼저 부분집합을 구해준다.
    subsets = [[]]
    result = []
    ## 다음 순회를 통해 만들 수 있는 모든 다리의 부분집합을 구한다
    for i in range(island):
        length = len(subsets)
        for j in range(len(subsets)):
            subsets.append(subsets[j] + [cost[i]])
    build(island)

    print(f'#{test_case} {result[0][0]} {result[0][1]}')
