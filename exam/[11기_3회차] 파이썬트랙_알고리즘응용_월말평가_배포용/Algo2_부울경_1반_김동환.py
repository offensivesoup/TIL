import sys
sys.stdin = open('algo2_sample_in.txt')

'''
어차피 최대 개수의 최소 비용으로 다리를 지어야하기 때문에
최대 개수의 최소비용의 다리가 지어진다면, 그것이 정답이 된다.
최소 비용의 다리가 지어지지 않는다면 그 개수의 다리는 아무것도 지을 수 없다.
'''

def build(cnt):
    # 기저조건
    ## 지을 수 있는 다리가 없다면
    if cnt == 0:
        print(f'#{test_case} 0 0')
        return

    # 지을 수 있다면
    if sum(cost[:cnt]) <= budget:
        # 출력
        print(f'#{test_case} {cnt} {sum(cost[:cnt])}')
        return

    # 안된다면 다리 개수를 줄여본다
    build(cnt - 1)

T = int(input())

for test_case in range(1, T+1):
    island, budget = map(int, input().split())  # 섬의 수와 예산
    result = 0
    cost = list(map(int, input().split()))  # 다리 각각에 대한 건설 비용
    cost.sort() # 비용순으로 나열되게 정렬해준다.
    build(island)