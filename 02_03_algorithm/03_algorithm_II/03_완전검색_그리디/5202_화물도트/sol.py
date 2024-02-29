import sys
sys.stdin = open('input.txt')

'''
도크가 설치되어있다
시작시간과 끝시간이 지정되어있을때,
하루에 도크를 최대한 활용하려면
'''

from collections import deque

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    times = [tuple(map(int,input().split())) for _ in range(N)]
    times.sort(key = lambda x : x[1])
    times = deque(times)
    working = [times[0]]
    cnt = 1
    while times:
        time = times.popleft()
        if working[-1][1] <= time[0]:
            cnt += 1
            working.append(time)
        else:
            continue
    print(f'#{test_case} {cnt}')










