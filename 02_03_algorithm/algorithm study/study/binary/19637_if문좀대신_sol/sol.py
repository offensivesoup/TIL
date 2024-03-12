import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())
naming = [tuple(input().split()) for _ in range(N)]
naming.sort(key=lambda x : int(x[1]))
powerLst=[int(input()) for _ in range(M)]

'''
문제 풀이의 순서
1. 일단 power를 하나씩 돌려봄
2. 근데 만약 그 power가 naming의 값보다 작거나 같으면
3. 된거임 그거 맞음
4. 근데 그게 아니면
5. 더 큰값에서 찾아보아야지
'''

for power in powerLst:
    start = 0
    end = N - 1
    result = 0 # 나온 mid를 담을 값
    while start <= end:
        mid = (start+end)//2
        if power <= int(naming[mid][1]): # 그게 첫번째꺼에 해당하는거네?
            result = mid
            end = mid - 1
        else: # 아니면
            start = mid + 1 # 전에꺼 보러 가자
    print(naming[result][0])

