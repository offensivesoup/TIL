import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    A, B = input().split() # A와 B문자열
    N, M = len(A), len(B)  # 각각의 길이
    cnt = A.count(B) # 겹치는 횟수
    result = N - ((M-1)*cnt)
    print(f'#{tc} {result}')