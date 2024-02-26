import sys
sys.stdin = open('algo2_sample_in.txt')

def find_best(i, k, n, visited): # 시작점, 꼭대기, 합, visited
    global maxi # 최고점을 전역변수에서 받아온다
    global cnt
    cnt+=1
    if i == k: # 만약 맨 마직막 줄에 도착했는데
        if n > maxi: # 그 때 점수의 합이 지금 맥시멈보다 크다
            maxi = n # 그럼 맥시멈 갱신
    elif n < maxi:
        return
    for j in range(N): # 순회를 돈다
        if not visited[j]: # 만약 그 열의 점수를 맞춘적이 없다면
            if shooting[i][j] < 0: # 근데 그 점수가 음수면
                continue # 지나쳐야해
            visited[j] = 1 # 음수가 아니면 방문표시
            find_best(i+1,k,n+shooting[i][j], visited) # 그리고 해당 점수를 더한 값을 누적합에 넣어준다
            visited[j] = 0 # 다녀오면 방문표시 해제

T = int(input())

for test_case in range(1,T+1):
    maxi = 0 # 출력하게될 최고 점수
    cnt = 0
    N = int(input()) # 사격판의 크기 입력
    shooting = [list(map(int,input().split())) for _ in range(N)] # 사격판
    visited = [0] * N # 같은 열이 안겹치도록 할 방문기록
    find_best(0,N,0,visited) # 함수에 대입
    print(f'#{test_case} {maxi}')
    print(cnt)