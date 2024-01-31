import sys
sys.stdin = open('input.txt')

## 단어가 대각선으로 들어가진 않으니까
## 행탐색과 열탐색을 각각해서 하나의 리스트로 담아내고
## 그 리스트를 순회하면서 (K만큼씩)

T = int(input())

for test_case in range(1,T+1): # 테스트 케이스의 횟수 반복
    N, K = map(int,input().split()) # 길이와 단어글자수 입력 받기
    words = [1] * K # 단어는 1로 채워지니, 단어 만들어주기
    area = [list(map(int,input().split())) for _ in range(N)] # 2차원 배열로 입력받기
    result = 0
    # 행부터 해보자
    for row in area: # 행을 순환한다.
        for i in range(len(row) -K + 1): # 글자수만큼 행을 볼 수 있게 한다
            if i == 0: # 만약 행의 첫부분이면
                if row[i:i+K] == words and row[i+K] == 0: # 글자 그 다음이 검정칸이면 가능
                    result += 1
            elif i == len(row) -K: # 만약 끝부분까지면
                if row[i-1] == 0 and row[i:i+K] == words: # 시작의 전 부분이 0 이면 가능
                    result += 1
            elif 0 < i < len(row) - K: # 중간 값이면
                if row[i-1] == 0 and row[i:i+K] == words and row[i+K] == 0: # 첫과 끝이 전과 다음값이 0 이면 가능
                    result += 1

    colLst = []
    for m in range(len(area)): # 열리스트를 만들어준다
        k = []
        for j in range(len(area)):
            k.append(area[j][m])
        colLst.append(k)

    for col in colLst: # 열도 행과 똑같은 흐름도로 간다.
        for m in range(len(col) -K + 1):
            if m == 0:
                if col[m:m+K] == words and col[m+K] == 0:
                    result += 1
            elif m == len(row) -K:
                if col[m-1] == 0 and col[m:m+K] == words:
                    result += 1
            elif 0 < m < len(col) - K:
                if col[m-1] == 0 and col[m:m+K] == words and col[m+K] == 0:
                    result += 1

    print(f'#{test_case} {result}')