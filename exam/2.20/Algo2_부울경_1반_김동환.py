T = int(input()) # 테스트 케이스 개수의 입력
for test_case in range(1,T+1): # 테스트 케이스 횟수 반복
    N, K = map(int,input().split()) # N(연잎의 개수), K(점프횟수) 입력
    leaves = list(map(int,input().split())) # 연잎 배열
    total_score = 0
    jump = leaves[0]  # 처음 점프 크기
    jumping = [] # 점프를 담을 리스트
    for i in range(K): # 정해진 횟수만큼 점프
        try:
            total_score += leaves[jump] # 현 연꽃의 점수를 담음
            jumping.append(leaves[jump]) # 점핑 했다는 리스트에 담아준다.
            jump = jump + leaves[jump] # 그다음 점프는 현재 점수만큼 점프하는 것이다
            if jump < 0 or jump > N-1:
                break # 만약 전체로 나가진다면
            if jumping[i-1] < 0 and jumping[i] > 0: # 만약 이전에 뒤로 뛰었는데, 앞으로 뛰게 되었다면
                jump = jump - jumping[i-1] # 이전점프만큼 앞으로 더 뛴다.
        except IndexError:
            break
    print(f'#{test_case} {total_score}') # 결과 출력






