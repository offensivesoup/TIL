import sys
sys.stdin = open('algo1_sample_in.txt')

T = int(input())

row = [1,-1,0,0] # 델타 탐색을 위한 row 배열
col = [0,0,-1,1] # 델타 탐색을 위한 col 배열

for test_case in range(1,T+1): # 테스트 케이스의 입력
    N = int(input()) # 배열의 크기 입력
    area = [list(map(int,input().split())) for _ in range(N)] # 총 사격 공간의 입력 2차원 배열
    scores = [] # 각 점수들을 반환
    for i in range(N-2,0,-1): # 행우선 탐색 (최소값이 0이기 때문에, 4지점 모두 사격할 수 있는 만큼만 range)
        for j in range(N-2,0,-1): # 열 탐색
            total = 0 # 각 사격지점의 합계를 담을 변수 생성
            for k in range(4): # 델타 탐색을 위한 반복구문
                total += area[i + row[k]][j + col[k]] # 각 지점의 반복구문 생성
            total -= area[i][j] # 맞춘지점의 점수를 뺀다.
            scores.append(total) # 해당 과녁을 맞춰 얻은 점수를 더해준다
    bonus_score = 0 # 보너스 점수를 계산
    maximum = 0 # 최고 보너스 점수를 담을 변수
    for score in scores: # 사용자가 얻은 점수 배열의 순회
        if score % 2 == 0 and score != 0: # 0이 아니면서 짝수이면
            bonus_score = score * 2 # 보너스 점수는 해당 점수의 2배
            if bonus_score > maximum: # 그 점수가 맥시멈 보다 크면
                maximum = bonus_score # 맥시멈 변수를 재할당
        elif score % 2 == 1: # 만약 홀수라면
            bonus_score = score # 보너스 점수는 해당 점수
            if bonus_score > maximum: # 그 점수가 맥시멈 보다 크면
                maximum = bonus_score # 맥시멈을 재할당
        else: # 그 외의 0점인 경우, 음수인 경우에는
            bonus_score = 0 # 보너스 점수는 0점이다.
    print(f'#{test_case} {maximum}') # 출력결과의 확인

