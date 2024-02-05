import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1): # 테스트 케이스 반복
    N = int(input()) # 몇개의 구역에 색칠할 것인지
    area = [[0] * 10 for _ in range(10)] # zero array 생성
    for i in range(N): # 색칠 횟수만큼 반복
        r1, c1, r2, c2, color = list(map(int,input().split())) # 한 구역 씩 색칠
        for row in range(r1,r2+1): # 행 순환
            for col in range(c1,c2+1): # 열 순환
                area[row][col] += color # 각 색깔 만큼 누적합

    result = 0 # 결과를 담을변수
    for j in range(len(area)): # 행우선 탐색
        for k in range(len(area[j])):
            if area[j][k] == 3: # 만약 색칠이 보라(3)으로 되어있다면
                result += 1 # 그 개수만큼 result에 할당
    print(f'#{test_case} {result}')