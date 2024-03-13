import sys
sys.stdin = open('input.txt')

'''
N개의 캐릭터, 각 캐릭터는 현재 X 레벨 최대 총합 K만큼 올릴 수 있다
최소를 최대로 만드는 법
'''
N, K = map(int,input().split())
levels = [int(input()) for _ in range(N)]
start, end = 1, 1e9 + 1
result = 0
while start <= end:
    mid = (start+end)//2 # 더해줄 수 있는 레벨
    sumi = 0 # 그떄의 합
    for level in levels: # 후보군을 뽑아줄게
        if mid >= level: # 만약 레벨이 값보다 작아 
            sumi += mid - level # 그러면 sumi 에 얼만큼 더해줬는지 나타내줄게
    if K >= sumi: # 다 돌았는데, 만약 sumi가 K 보다 작다 -> 더할 수 있는 여지가 있다 
        result = mid # 일단 지금의 최대값이니까 결과에 주고
        start = mid + 1 # 조금 더 더해볼게
    else: # 아니면
        end = mid - 1 # 조금 덜 더해줘야 할거같애
print(int(result)) # 마지막 result를 정수형으로 출력

