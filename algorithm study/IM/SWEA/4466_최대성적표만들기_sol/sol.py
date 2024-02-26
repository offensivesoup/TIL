import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    N, K = map(int,input().split())
    scores = list(map(int,input().split()))
    result = 0
    for k in range(K):
        result += max(scores)
        scores.remove(max(scores))
    print(f'#{test_case} {result}')

