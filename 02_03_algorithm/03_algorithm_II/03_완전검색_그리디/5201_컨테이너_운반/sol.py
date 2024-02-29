import sys
sys.stdin = open('input.txt')

'''
트럭당 하나의 컨테이너 운반
최대가 되도록 컨테이너를 옮기면, 화물의 전체 무게가 얼마인지 출력
화물을 싣지 못한 트럭이 있거나, 남는 화물이 있을 수도 있고, 아에 못옮기면 0
그럼 젤 큰 트럭부터 차곡차곡 쌓아나가면 안될까
'''

T = int(input())
for test_case in range(1,T+1):
    maxi = 0
    N, M = map(int,input().split()) # 화물의 개수, 트럭의 대수
    containers  = list(map(int,input().split())) # 화물의 무게
    trucks = list(map(int,input().split())) # 트럭의 적재 용량
    containers.sort(reverse=True)
    trucks.sort(reverse=True)
    for truck in trucks:
        for container in containers:
            if truck >= container:
                maxi += container
                containers.remove(container)
                break # 실으면 다음 트럭 봐야함
    print(f'#{test_case} {maxi}')









