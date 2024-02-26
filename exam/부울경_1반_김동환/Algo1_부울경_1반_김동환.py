T= int(input())
row_move = [-2,-1,1,2,0,0,0,0] # 보너스 점수를 탐색하기 위한 리스트
col_move = [0,0,0,0,-2,-1,1,2]

for test_case in range(1,T+1):
    N = int(input())
    maxi  = 0 # 출력할 최대값
    aij = [list(map(int,input().split())) for _ in range(N)] # 과녁판
    for i in range(N):
        for j in range(N):
            bonus = aij[i][j]  # 점수를 담을 값
            for m in range(8): # 보너스 점수를 탐색한다
                row = row_move[m] + i # 행과
                col = col_move[m] + j # 열을 지정한다
                if 0 <= row < N and 0 <= col < N: # 그 값들이 인덱스 범위 내라면
                    bonus += aij[row][col] # 보너스에 해당점수를 더해준다
            if bonus > maxi: # 그렇게 완성된 보너스점수가 현재까지의 최대값보다 크다면
                maxi = bonus # 최대값을 갱신한다
    print(f'#{test_case} {maxi}')
