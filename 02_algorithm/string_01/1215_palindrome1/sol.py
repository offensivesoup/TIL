import sys
sys.stdin = open('input.txt')

for test_case in range(1,11):
    M = 8 # 배열의 크기 M * M
    N = int(input())  # 찾아야 하는 글자 수
    arr = [input() for _ in range(M)] # 글자 입력받기
    area = [list(x) for x in arr] # 입력받은 글자로 2차원 리스트 만들기
    # 전치행렬된 reverse 생성
    reverse_area = [[0] * M for _ in range(M)]
    for h in range(M): # 전치행렬 시키기
        for v in range(M):
            reverse_area[h][v], reverse_area[v][h] = area[v][h], area[h][v]
    idx = 0
    sumi = 0 # 회문을 더해줄 값
    # 글자수만큼의 회문 찾기
    for i in range(M-N+1):
        for j in range(M):
            hword = area[j][i:i + N] # 가로 단어
            vword = reverse_area[j][i:i + N] # 세로 단어
            if hword == hword[::-1]: # 가로 회문 검사
                sumi += 1
            if vword == vword[::-1]: # 세로 회문 검사
                sumi += 1
    print(f'#{test_case} {sumi}') # 결과 출력




