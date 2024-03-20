import sys
sys.stdin = open('input.txt')

'''
자연수 N에 몇번의 연산을 통해 다른 자연수 M
사용할 연산이 +1, -1, *2, -10 4가지이다.
단 연산의 중간 결과도 항상 백만 이하의 자연수이다.
N = 2, M = 7 인 경우, (2 + 1) * 2 + 1 = 7 이므로 최소 3번의 연산이다
'''

from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    result = 0
    que = deque([(N, 0)])
    visited = [0] * 1000001
    while que:
        N, cnt = que.popleft()
        if visited[N]:
            continue
        visited[N] = 1
        if N == M:
            result = cnt
            break
        else:
            if 0 < N + 1 <= 1000000:
                que.append((N + 1, cnt + 1))
            if 0 < N - 1 <= 1000000:
                que.append((N - 1, cnt + 1))
            if 0 < N * 2 <= 1000000:
                que.append((N * 2, cnt + 1))
            if 0 < N - 10 <= 1000000:
                que.append((N - 10, cnt + 1))
    print(f'#{tc} {result}')



