import sys
sys.stdin = open('input.txt')

def back(row, n, now_sum, visited):
    global mini # 일단 최소값 가져와서
    if row == n: # 행이 끝에 다달았는데
        if now_sum < mini: # 그때 다 더해진게 지금의 최소값 보다 작아
            mini = now_sum # 그럼 최소값 갱신 후
            return # 종료
    elif now_sum >= mini: # 근데 끝 까지 안갔는데도 지금까지 더한게 더 커
        return # 그럼 더 볼 필요 없어
    else: # 둘다 아니면
        for col in range(N): # 탐색해본다
            if not visited[col]: # 만약 그게 전 공장에서 만들기로 한 물품이 아니면
                visited[col] = 1 # 그건 내가 만든다고 표시한다
                back(row+1, n, now_sum+factory[row][col], visited) # 그리고 재귀함수에 (다음행, 끝점(동일), 지금까지 더한거에 현재 만들기로 한거 더한 값, 만들었다는 표시 넘겨준다)
                visited[col] = 0 # 재귀 다녀오면 다시 초기화 시킨다.

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    factory = [list(map(int,input().split())) for _ in range(N)] # 공장을 만들어줌
    visited = [0] * N # 방문표시 해줄거야 ( 배열최소합 처럼 )
    mini = 1e9 # 갱신시킬 최소값 선언
    back(0,N,0,visited) # 백트래킹 시작
    print(f'#{tc} {mini}') # 최소값 출력