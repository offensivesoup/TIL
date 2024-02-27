import sys
sys.stdin = open('input.txt')

'''
종점인 N번 정류장
한번 충전으로 최대한 이동할 수 있는 K가 정해져있다(배터리)
충전기가 설치된 M개의 정류장 번호가 주어지면
최소 몇번은 충전해야 N에 도착할 수 있는지
만약 충전기가 잘못설치되어 종점에 갈 수 없으면 0 ()
'''

T = int(input())

for test_case in range(1,T+1):
    K, N, M = map(int,input().split()) # K = 한번에 이동할 수 있는 양, N = 종점, M = 충전기 개수
    charging = list(map(int,input().split()))
    full = K
    result = 0
    # 충전을 할지 말지 결정하는 것이 중요하다.
    # 현위치에서 한칸 씩 이동한다.
    n = 0  # 첫번쨰 정류장 인덱스
    for i in range(1,N): # 한칸씩 이동
        K -= 1 # 갈수 있는양이 줄어든다.
        if K < 0 and i != N: # 연료 다 떨어짐
            result = 0
            break
        if i == charging[len(charging) - 1]:
            if K < N - i:
                result += 1
                break
        if i == charging[n]: # 충전소에 도착
            if K < charging[n + 1] - i: # 다음 충전소보다 K가 작음
                K = full # 충전함
                result += 1 # 충전횟수 1 더함
                n += 1
                if n == len(charging) -1:
                    n -= 1
            elif K >= charging[n + 1] - i:
                n += 1
                if n == len(charging) - 1:
                    n -= 1
    print(f'#{test_case} {result}')



