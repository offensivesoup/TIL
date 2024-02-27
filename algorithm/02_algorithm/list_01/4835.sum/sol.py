import sys
sys.stdin = open('input.txt')


T = int(input())

for test_case in range(1,T+1):
    result = []
    N, M = map(int,input().split())
    sum_arr = list(map(int,input().split())) # 입력을 받는다
    for i in range(len(sum_arr)):
        if len(sum_arr[i:i+M]) == M:
            result.append(sum(sum_arr[i:i+M]))
    print(f'#{test_case} {max(result) - min(result)}')