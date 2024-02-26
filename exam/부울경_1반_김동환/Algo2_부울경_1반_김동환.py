T = int(input())

for test_case in range(1,T+1):
    N, M = map(int,input().split())
    total_arr = [list(map(int,input().split())) for _ in range(N)] # 시작할 배열 입력받기
    start_row, start_col = 0, 0 # 최대값을 찾은 이후의 탐색 시작점을 담을 변수
    maxiLst = [] # 최대값을 담을 변수
    startLst = [] # 최대값이 나온 인덱스들을 담을 변수
    while True: # 반복문
        maxi = -101 # 새롭게 찾은 최대값을 담아줄 변수
        for i in range(start_row,start_row+M): # 탐색된 최대값을 시작점으로 탐색시작
            for j in range(start_col,start_col+M):
                if 0 <= i < N and 0 <= j < N: # 탐색범위 설정
                    if maxi < total_arr[i][j]: # 탐색한 값이 최대값이라면
                        maxi = total_arr[i][j] # 최대값에 담는다
                        startLst.append(i) # 그 인덱스 또한 담는다
                        startLst.append(j)
        start_row = startLst[-2] # 해당 배열에서 가장 큰 값의 인덱스
        start_col = startLst[-1]
        maxiLst.append(maxi) # 나온 최대값을 리스트에 담아준다
        if len(maxiLst) > 1: # 찾은 최대값이 첫 최대값이 아니고
            if maxiLst[-1] == maxiLst[-2]: # 새로운 최대값을 찾지 못했다면,(해당 배열에서 찾은 최대값이 이전에 찾은 최대값과 같다면)
                break # 종료한다
    print(f'#{test_case} {sum(maxiLst[:-1])}') # 그렇게 만들어진 끝나기 직전까지의 최대값의 합을 반환한다.
