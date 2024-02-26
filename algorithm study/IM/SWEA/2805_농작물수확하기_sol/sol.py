import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    farm = [list(map(int,input())) for _ in range(N)]
    benefit = 0
    start = 0 # 시작지점(행 지정)
    end = N-1
    middle = N//2 # 행의 가운데
    left, right = 0, 1
    while start <= end:
        if start != end:
            benefit += sum(farm[start][middle + left: middle + right])
            benefit += sum(farm[end][middle + left: middle + right])
            start += 1
            end -= 1
            left -= 1
            right += 1
        else:
            benefit += sum(farm[start][middle + left: middle + right])
            break
    print(f'#{test_case} {benefit}')

            
        
