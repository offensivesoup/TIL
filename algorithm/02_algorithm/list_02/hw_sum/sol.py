import sys
sys.stdin = open('input.txt')

T = 10
N = 100
for test_case in range(1,T+1): # 테스트 케이스 반복
    M = input() # 각 테스트 케이스의 번호를 입력 받는다
    arr = [list(map(int,input().split())) for _ in range(100)] # 입력된 100 * 100의 2차원 배열 출력
    sumLst = [] # 각 합을 append 할 리스트 선언
    ijSum = 0  # 왼쪽 위에서 오른쪽 아래 대각선
    jiSum = 0  # 오른쪽 위에서 왼쪽 아래 대각선
    for i in range(len(arr)):
        jSum = 0 # 세로의 합 순환시 마다 초기화
        ijSum += arr[i][i] # 왼쪽에서 오른쪽 대각선 추가
        jiSum += arr[i][-i-1] # 오른쪽에서 왼쪽으로 추가
        sumLst.append(sum(arr[i])) # 각 행(가로)의 합 추가
        for j in range(len(arr)):
            jSum += arr[j][i] # 각 열 순회한 값 더하기
        sumLst.append(jSum)
    sumLst.append(jiSum) # 각 대각선의 합 추가
    sumLst.append(ijSum)
    print(f'#{test_case} {max(sumLst)}')











