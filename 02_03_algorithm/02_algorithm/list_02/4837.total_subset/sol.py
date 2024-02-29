import sys
sys.stdin = open('input.txt')

T = int(input())
A = list(range(1,13)) # 1 ~ 12 까지의 배열인 A
for test_case in range(1,T+1): # 테스트 케이스 반복
    N, K = map(int,input().split()) # N 개의 길이면서, K개의 합 입력
    result = 0 # 결과를 담을 result 변수
    for i in range(1, 1 << len(A)): # 1 << A의 길이만큼 보내 2진수로 하나의 인덱싱마다 값 배정
        tmpLst = [] # 부분집합을 담을리스트
        for j in range(len(A)): # 부분집합 생성
            if i & (1<<j):
                tmpLst.append(A[j]) # 리스트에 담기
        if len(tmpLst) == N and sum(tmpLst) == K: # N개의 길이이면서 K의 합인 경우 조건처리
            result += 1 # result에 1씩 덧셈
    print(f'#{test_case} {result}') # 결과 확인



